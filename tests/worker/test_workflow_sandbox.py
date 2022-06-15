import uuid
from dataclasses import dataclass
from typing import Callable, Dict, Iterable, List, Optional, Type

from temporalio import workflow
from temporalio.client import Client
from temporalio.exceptions import ApplicationError
from temporalio.worker import SandboxedWorkflowRunner, UnsandboxedWorkflowRunner, Worker
from tests.worker import stateful_module
from tests.worker.test_workflow import assert_eq_eventually

global_state = ["global orig"]


@dataclass
class GlobalStateWorkflowParams:
    fail_on_first_attempt: bool = False


@workflow.defn
class GlobalStateWorkflow:
    def __init__(self) -> None:
        self.append("inited")

    @workflow.run
    async def run(self, params: GlobalStateWorkflowParams) -> Dict[str, List[str]]:
        self.append("started")
        if params.fail_on_first_attempt:
            raise ApplicationError("Failing first attempt")
        # Wait for "finish" to be in the state
        await workflow.wait_condition(lambda: "finish" in global_state)
        return self.state()

    @workflow.signal
    def append(self, str: str) -> None:
        global_state.append(str)
        stateful_module.module_state.append(str)

    @workflow.query
    def state(self) -> Dict[str, List[str]]:
        return {"global": global_state, "module": stateful_module.module_state}


async def test_workflow_sandbox_global_state(client: Client):
    async with new_worker(client, GlobalStateWorkflow) as worker:
        # Run it twice sandboxed and check that the results don't affect each
        # other
        handle1 = await client.start_workflow(
            GlobalStateWorkflow.run,
            GlobalStateWorkflowParams(),
            id=f"workflow-{uuid.uuid4()}",
            task_queue=worker.task_queue,
        )
        handle2 = await client.start_workflow(
            GlobalStateWorkflow.run,
            GlobalStateWorkflowParams(),
            id=f"workflow-{uuid.uuid4()}",
            task_queue=worker.task_queue,
        )
        # Wait until both started so our signals are _after_ start
        async def handle1_started() -> bool:
            return (
                "started" in (await handle1.query(GlobalStateWorkflow.state))["global"]
            )

        async def handle2_started() -> bool:
            return (
                "started" in (await handle1.query(GlobalStateWorkflow.state))["global"]
            )

        await assert_eq_eventually(True, handle1_started)
        await assert_eq_eventually(True, handle2_started)

        await handle1.signal(GlobalStateWorkflow.append, "signal1")
        await handle2.signal(GlobalStateWorkflow.append, "signal2")

        await handle1.signal(GlobalStateWorkflow.append, "finish")
        await handle2.signal(GlobalStateWorkflow.append, "finish")

        # Confirm state is as expected
        assert {
            "global": ["global orig", "inited", "started", "signal1", "finish"],
            "module": ["module orig", "inited", "started", "signal1", "finish"],
        } == await handle1.result()
        assert {
            "global": ["global orig", "inited", "started", "signal2", "finish"],
            "module": ["module orig", "inited", "started", "signal2", "finish"],
        } == await handle2.result()

        # But that _this_ global state wasn't even touched
        assert global_state == ["global orig"]
        assert stateful_module.module_state == ["module orig"]


# TODO(cretz): To test:
# * Invalid modules
# * Invalid module members (all forms of access/use)
# * Different preconfigured passthroughs


def new_worker(
    client: Client,
    *workflows: Type,
    activities: Iterable[Callable] = [],
    task_queue: Optional[str] = None,
    sandboxed: bool = True,
) -> Worker:
    return Worker(
        client,
        task_queue=task_queue or str(uuid.uuid4()),
        workflows=workflows,
        activities=activities,
        workflow_runner=SandboxedWorkflowRunner()
        if sandboxed
        else UnsandboxedWorkflowRunner(),
    )
