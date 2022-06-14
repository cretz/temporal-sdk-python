
from typing import Callable, Iterable, Optional, Type
import uuid
from temporalio.client import Client
from temporalio.worker import Worker, SandboxedWorkflowRunner, UnsandboxedWorkflowRunner
from tests.worker.sandbox_workflows import workflow_threading, workflow_global_state


async def test_workflow_sandbox_threading(client: Client):
    async with new_worker(client, workflow_threading.Workflow) as worker:
        await client.execute_workflow(
            workflow_threading.Workflow.run,
            id=f"workflow-{uuid.uuid4()}",
            task_queue=worker.task_queue,
        )

async def test_workflow_sandbox_global_state(client: Client):
    async with new_worker(client, workflow_global_state.Workflow) as worker:
        # Run it twice sandboxed and check that the results don't affect each
        # other
        result1 = await client.execute_workflow(
            workflow_global_state.Workflow.run,
            workflow_global_state.WorkflowParams(),
            id=f"workflow-{uuid.uuid4()}",
            task_queue=worker.task_queue,
        )
        result2  = await client.execute_workflow(
            workflow_global_state.Workflow.run,
            workflow_global_state.WorkflowParams(),
            id=f"workflow-{uuid.uuid4()}",
            task_queue=worker.task_queue,
        )
        print(f"RESULT1: {result1}")
        print(f"RESULT2: {result2}")


def new_worker(
    client: Client,
    *workflows: Type,
    activities: Iterable[Callable] = [],
    task_queue: Optional[str] = None,
    sandboxed: bool = True
) -> Worker:
    return Worker(
        client,
        task_queue=task_queue or str(uuid.uuid4()),
        workflows=workflows,
        activities=activities,
        workflow_runner=SandboxedWorkflowRunner() if sandboxed else UnsandboxedWorkflowRunner(),
    )