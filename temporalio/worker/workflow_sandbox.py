from __future__ import annotations
import dataclasses
import sys
import types
from typing import Any, Callable, Dict, List, Mapping, Optional, Sequence, Tuple, Type, Union
from .workflow_instance import UnsandboxedWorkflowRunner, WorkflowInstance, WorkflowInstanceDetails, WorkflowRunner
import temporalio.bridge.proto.workflow_activation
import temporalio.bridge.proto.workflow_completion
from typing_extensions import TypeAlias
import importlib
import importlib.abc
import importlib.util
import importlib.machinery

# Possible approaches:
#   1 - No sys modules except sys, import uses importlib.import_module. Problem
#       with this approach and the next is it replaces __import__ and not the
#       true
#   2 - All existing modules copied, import uses importlib.reload except sys
#     * Problem - Using reload does not clear globals :-(
# Failed approaches:
#   * Using sysaudit callbacks - They do not catch all calls, so I couldn't
#     prevent datetime.now()
#   * Restricting imports via sys.metapath - We don't want to restrict imports
#     usually since many modules we want to allow import but restrict a couple
#     of calls. If we did want to restrict imports, we could do that in the
#     importer.
APPROACH = 1
# TODO(cretz): Have a concept of an import spec which has:
# * Modules which can pass through - don't need to be reloaded because we
#   know they are side-effect free
# * Modules that can never be even imported - only because the mere fact of
#   importing them can cause irreparable side effects (this is rare, unsure if
#   we will ever set this)
# * Module reload details - Fnmatch that can match vars (prevent getter/setter
#   access), functions, or class methods (includes __init__)

class SandboxedWorkflowRunner(WorkflowRunner):
    def __init__(self, underlying: WorkflowRunner = UnsandboxedWorkflowRunner()) -> None:
        super().__init__()
        self._underlying = underlying
        # Install the restricted importer at the beginning of the meta path if
        # not already there
        # importer = _RestrictedImporter.instance()
        # if importer not in sys.meta_path:
        #     sys.meta_path.insert(0, importer)


    async def create_instance(self, det: WorkflowInstanceDetails) -> WorkflowInstance:
        instance = _WorkflowInstanceImpl(self._underlying, det)
        await instance.initialize()
        return instance

class _WorkflowInstanceImpl(WorkflowInstance):
    def __init__(self, underlying: WorkflowRunner, det: WorkflowInstanceDetails) -> None:
        super().__init__()
        self._underlying = underlying
        self._det = det
        self._sandboxed_class: Optional[Type] = None

        # TODO(cretz): Customize better
        self._real_import = __import__
        # Builtins not properly typed in typeshed
        assert isinstance(__builtins__, dict)
        new_builtins = __builtins__.copy()
        new_builtins["__import__"] = self._sandboxed_import
        self._globals_and_locals = {
            # TODO(cretz): Change __import__ here to add our restrictions
            # TODO(cretz): Remove builtins we don't like
            "__builtins__": new_builtins,
            "__temporal_instance": self,
            # TODO(cretz): Other special variables
            # TODO(cretz): Any harm in just hardcoding this?
            "__file__": "workflow_sandbox.py",
        }

        # Import and create the instance
        create_source = (
            # Execute preamble
            # "import sys\n"
            # "print('MODS:', list(sys.modules.keys()))\n"
            # "print('META PATH', sys.meta_path)\n"
            "__temporal_instance._sandboxed_preamble()\n"
            # Import the definition class
            f"from {det.defn.cls.__module__} import {det.defn.cls.__name__} as __temporal_workflow_class\n"
            "__temporal_instance._sandboxed_class = __temporal_workflow_class\n"
            # "print('MODS4:', list(sys.modules.keys()))\n"
        )
        print("PRE-EXEC", sys.meta_path)
        # Remove module cache and replace when done
        # TODO(cretz): Are there some modules we have that we want to keep
        # cached?
        self._old_modules = sys.modules
        old_dont_write_bytecode = sys.dont_write_bytecode
        sys.dont_write_bytecode = True
        old_cache_tag = sys.implementation.cache_tag
        sys.implementation.cache_tag = None
        
        old_meta_path = sys.meta_path
        # TODO(cretz): Wut
        sys.meta_path = [_RestrictedImporter(old_meta_path)]
        # sys.meta_path = sys.meta_path.copy()
        # sys.meta_path.insert(0, _RestrictedImporter(old_meta_path))

        # old_path_importer_cache = sys.path_importer_cache
        # sys.path_importer_cache = {}
        importlib.invalidate_caches()
        importlib.machinery.PathFinder.invalidate_caches()
        if APPROACH == 1:
            # sys.modules = {"sys": sys, "builtins": sys.modules["builtins"] } # "dataclasses": dataclasses}
            sys.modules = { }
        else:
            sys.modules = sys.modules.copy()
        self._reloaded: Dict[str, bool] = {}
        try:
            exec(create_source, self._globals_and_locals, self._globals_and_locals)
        finally:
            sys.modules = self._old_modules
            sys.meta_path = old_meta_path
            sys.dont_write_bytecode = old_dont_write_bytecode
            sys.implementation.cache_tag = old_cache_tag
        print("POST-EXEC")

    async def initialize(self) -> None:
        # Do the underlying create instance with our sandboxed class
        new_det = dataclasses.replace(self._det, defn=dataclasses.replace(self._det.defn, cls=self._sandboxed_class))
        self._instance = await self._underlying.create_instance(new_det)

    def activate(self, act: temporalio.bridge.proto.workflow_activation.WorkflowActivation) -> temporalio.bridge.proto.workflow_completion.WorkflowActivationCompletion:
        print("PRE-ACT")
        # old_modules = sys.modules
        # sys.modules = {}
        # try:
        return self._instance.activate(act)
        # finally:
        #     sys.modules = old_modules
        #     print("POST-ACT")

    def _sandboxed_preamble(self) -> None:
        # print("MODS2:", list(sys.modules))
        # print("MODS3:", list(sys2.modules))
        # Replace all modules which removes cached modules
        # sys.modules = {
        #     "sys": sys.modules["sys"],
        #     "builtins": sys.modules["builtins"],
        #     # TODO(cretz): Needed because importing it checks sys.modules["warnings"]
        #     "warnings": sys.modules["warnings"],
        #     # TODO(cretz): Inspect expects this key
        #     "__main__": None, # type: ignore
        # }
        # TODO(cretz): Disable any other modules?
        # sys.modules["importlib"] = None
        # sys.addaudithook(self._sandboxed_audit_hook)
        pass

    def _sandboxed_audit_hook(self, event: str, args: Tuple) -> None:
        print("HOOK THING: ", event, args)

    def _sandboxed_import(
        self,
        name: str,
        globals: Optional[Mapping[str, object]] = None,
        locals: Optional[Mapping[str, object]] = None,
        fromlist: Sequence[str] = (),
        level: int = 0,
    ) -> types.ModuleType:
        print("IMPORT: ", name, fromlist, name in self._old_modules, name in sys.modules, name in self._reloaded)
        if APPROACH == 1:
            if name in self._old_modules and name not in sys.modules:
                print("RELOAD!", sys.meta_path)
                try:
                    return importlib.import_module(name)
                    # return importlib.__import__(name, globals, locals, fromlist, level)
                    # return self._real_import(name, globals, locals, fromlist, level)
                finally:
                    print("RELOAD DONE!")
        else:
            if name in sys.modules and name not in self._reloaded:
                print("RELOAD!")
                self._reloaded[name] = True
                return importlib.reload(sys.modules[name])
        return self._real_import(name, globals, locals, fromlist, level)


class _RestrictedImporter(importlib.abc.MetaPathFinder):
    _instance: Optional[_RestrictedImporter] = None

    # @staticmethod
    # def instance() -> _RestrictedImporter:
    #     if _RestrictedImporter._instance is None:
    #         _RestrictedImporter._instance = _RestrictedImporter()
    #     return _RestrictedImporter._instance

    def __init__(self, old_meta_path: List[Any]) -> None:
        super().__init__()
        self._old_meta_path = old_meta_path

    def find_spec(
        self,
        fullname: str,
        path: Optional[Sequence[Union[bytes, str]]],
        target: Optional[types.ModuleType] = None,
    ) -> Optional[importlib.machinery.ModuleSpec]:
        print("RESTRICT IMPORT: ", fullname, path, target)
        for finder in self._old_meta_path:
            spec: importlib.machinery.ModuleSpec = finder.find_spec(fullname, path, target)
            if spec:
                # Copy the whole module but remove the cache
                print("FOUND", finder, spec.cached, spec.loader)
                return spec
                # importlib.util.spec_from_file_location
                # return importlib.util.spec_from_loader(spec.name, spec.loader, origin=spec.origin)
                # return importlib.machinery.ModuleSpec(
                #     spec.name, spec.loader, origin=spec.origin, loader_state=spec.loader_state,
                #     is_package=spec.submodule_search_locations is not None)
        print("NOT FOUND")
        return None

    # def find_module(self, fullname: str, path: Optional[Sequence[Union[bytes, str]]]) -> Optional[importlib.abc.Loader]:
    #     print("RESTRICT FIND: ", fullname, path)
    #     return None