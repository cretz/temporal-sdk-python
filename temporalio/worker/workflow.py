from __future__ import annotations

import asyncio
import concurrent.futures
import logging
from datetime import timezone
from typing import Callable, Dict, Iterable, List, Optional, Type

import temporalio.activity
import temporalio.api.common.v1
import temporalio.bridge.client
import temporalio.bridge.proto
import temporalio.bridge.proto.activity_result
import temporalio.bridge.proto.child_workflow
import temporalio.bridge.proto.common
import temporalio.bridge.proto.workflow_activation
import temporalio.bridge.proto.workflow_commands
import temporalio.bridge.proto.workflow_completion
import temporalio.bridge.worker
import temporalio.client
import temporalio.common
import temporalio.converter
import temporalio.exceptions
import temporalio.workflow
import temporalio.workflow_service

from .interceptor import Interceptor, WorkflowInboundInterceptor
from .workflow_instance import WorkflowInstance, WorkflowInstanceDetails, WorkflowRunner

logger = logging.getLogger(__name__)

LOG_PROTOS = False
DEADLOCK_TIMEOUT_SECONDS = 2


class _WorkflowWorker:
    def __init__(
        self,
        *,
        bridge_worker: Callable[[], temporalio.bridge.worker.Worker],
        namespace: str,
        task_queue: str,
        workflows: Iterable[Type],
        workflow_task_executor: Optional[concurrent.futures.ThreadPoolExecutor],
        workflow_runner: WorkflowRunner,
        data_converter: temporalio.converter.DataConverter,
        interceptors: Iterable[Interceptor],
        type_hint_eval_str: bool,
        max_concurrent_workflow_tasks: int,
    ) -> None:
        self._bridge_worker = bridge_worker
        self._namespace = namespace
        self._task_queue = task_queue
        self._workflow_task_executor = (
            workflow_task_executor
            or concurrent.futures.ThreadPoolExecutor(
                max_workers=max_concurrent_workflow_tasks,
                thread_name_prefix="temporal_workflow_",
            )
        )
        self._workflow_task_executor_user_provided = workflow_task_executor is not None
        self._workflow_runner = workflow_runner
        self._data_converter = data_converter
        self._interceptor_classes: List[Type[WorkflowInboundInterceptor]] = []
        for i in interceptors:
            interceptor_class = i.workflow_interceptor_class()
            if interceptor_class:
                self._interceptor_classes.append(interceptor_class)
        self._type_hint_eval_str = type_hint_eval_str
        self._running_workflows: Dict[str, WorkflowInstance] = {}

        # Validate and build workflow dict
        self._workflows: Dict[str, temporalio.workflow._Definition] = {}
        for workflow in workflows:
            defn = temporalio.workflow._Definition.must_from_class(workflow)
            # Confirm name unique
            if defn.name in self._workflows:
                raise ValueError(f"More than one workflow named {defn.name}")
            self._workflows[defn.name] = defn

    async def run(self) -> None:
        # Continually poll for workflow work
        task_tag = object()
        try:
            while True:
                act = await self._bridge_worker().poll_workflow_activation()
                # Schedule this as a task, but we don't need to track it or
                # await it. Rather we'll give it an attribute and wait for it
                # when done.
                task = asyncio.create_task(self._handle_activation(act))
                setattr(task, "__temporal_task_tag", task_tag)
        except temporalio.bridge.worker.PollShutdownError:
            return
        except Exception:
            # Should never happen
            logger.exception(f"Workflow runner failed")
        finally:
            # Collect all tasks and wait for them to complete
            our_tasks = [
                t
                for t in asyncio.all_tasks()
                if getattr(t, "__temporal_task_tag", None) is task_tag
            ]
            await asyncio.wait(our_tasks)
            # Shutdown the thread pool executor if we created it
            if not self._workflow_task_executor_user_provided:
                self._workflow_task_executor.shutdown()

    async def _handle_activation(
        self, act: temporalio.bridge.proto.workflow_activation.WorkflowActivation
    ) -> None:
        global LOG_PROTOS, DEADLOCK_TIMEOUT_SECONDS

        # Decode the activation if there's a codec
        if self._data_converter.payload_codec:
            await temporalio.bridge.worker.decode_activation(
                act, self._data_converter.payload_codec
            )

        if LOG_PROTOS:
            logger.debug("Received workflow activation: %s", act)
        completion = (
            temporalio.bridge.proto.workflow_completion.WorkflowActivationCompletion(
                run_id=act.run_id
            )
        )

        # Build completion
        try:
            # If the workflow is not running yet, create it
            workflow = self._running_workflows.get(act.run_id)
            if not workflow:
                workflow = await self._create_workflow_instance(act)
                self._running_workflows[act.run_id] = workflow

            # Run activation in separate thread so we can check if it's
            # deadlocked
            activate_task = asyncio.get_running_loop().run_in_executor(
                self._workflow_task_executor,
                workflow.activate,
                act,
            )

            # Wait for deadlock timeout and set commands if successful
            try:
                commands = await asyncio.wait_for(
                    activate_task, DEADLOCK_TIMEOUT_SECONDS
                )
                # TODO(cretz): Is this copy too expensive?
                completion.successful.commands.extend(commands)
            except asyncio.TimeoutError:
                raise RuntimeError(
                    f"Potential deadlock detected, workflow didn't yield within {DEADLOCK_TIMEOUT_SECONDS} second(s)"
                )
        except Exception as err:
            logger.exception(f"Failed activation on workflow with run ID {act.run_id}")
            # Set completion failure
            completion.failed.failure.SetInParent()
            try:
                temporalio.exceptions.apply_exception_to_failure(
                    err,
                    self._data_converter.payload_converter,
                    completion.failed.failure,
                )
            except Exception as inner_err:
                logger.exception(
                    f"Failed converting activation exception on workflow with run ID {act.run_id}"
                )
                completion.failed.failure.message = (
                    f"Failed converting activation exception: {inner_err}"
                )

        # Encode the completion if there's a codec
        if self._data_converter.payload_codec:
            await temporalio.bridge.worker.encode_completion(
                completion, self._data_converter.payload_codec
            )

        # Send off completion
        if LOG_PROTOS:
            logger.debug("Sending workflow completion: %s", completion)
        try:
            await self._bridge_worker().complete_workflow_activation(completion)
        except Exception:
            # TODO(cretz): Per others, this is supposed to crash the worker
            logger.exception(
                f"Failed completing activation on workflow with run ID {act.run_id}"
            )

        # If there is a remove-from-cache job, do so
        remove_job = next(
            (j for j in act.jobs if j.HasField("remove_from_cache")), None
        )
        if remove_job:
            logger.debug(
                f"Evicting workflow with run ID {act.run_id}, message: {remove_job.remove_from_cache.message}"
            )
            del self._running_workflows[act.run_id]

    async def _create_workflow_instance(
        self, act: temporalio.bridge.proto.workflow_activation.WorkflowActivation
    ) -> WorkflowInstance:
        # First find the start workflow job
        start_job = next((j for j in act.jobs if j.HasField("start_workflow")), None)
        if not start_job:
            raise RuntimeError("Missing start workflow")

        # Get the definition
        defn = self._workflows.get(start_job.start_workflow.workflow_type)
        if not defn:
            workflow_names = ", ".join(sorted(self._workflows.keys()))
            raise temporalio.exceptions.ApplicationError(
                f"Workflow class {start_job.start_workflow.workflow_type} is not registered on this worker, available workflows: {workflow_names}",
                type="NotFoundError",
            )

        # Build info
        start = start_job.start_workflow
        info = temporalio.workflow.Info(
            attempt=start.attempt,
            cron_schedule=start.cron_schedule or None,
            execution_timeout=start.workflow_execution_timeout.ToTimedelta()
            if start.HasField("workflow_execution_timeout")
            else None,
            namespace=self._namespace,
            run_id=act.run_id,
            run_timeout=start.workflow_run_timeout.ToTimedelta()
            if start.HasField("workflow_run_timeout")
            else None,
            start_time=act.timestamp.ToDatetime().replace(tzinfo=timezone.utc),
            task_queue=self._task_queue,
            task_timeout=start.workflow_task_timeout.ToTimedelta(),
            workflow_id=start.workflow_id,
            workflow_type=start.workflow_type,
        )

        # Create instance from details
        return await self._workflow_runner.create_instance(
            WorkflowInstanceDetails(
                payload_converter_class=self._data_converter.payload_converter_class,
                interceptor_classes=self._interceptor_classes,
                defn=defn,
                info=info,
                type_hint_eval_str=self._type_hint_eval_str,
            )
        )