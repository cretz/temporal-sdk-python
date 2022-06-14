
print("IMPORT BEGIN")
# from dataclasses import dataclass
import dataclasses
from temporalio.exceptions import ApplicationError
from tests.worker.sandbox_workflows import stateful_module

from temporalio import workflow

global_state = "global orig"

print("DATACLASS BEGIN")

@dataclasses.dataclass
class WorkflowParams:
    fail_on_first_attempt: bool = False

print("DATACLASS END")

@workflow.defn
class Workflow:
    @workflow.run
    async def run(self, params: WorkflowParams) -> str:
        global global_state
        global_state += ", modified"
        stateful_module.some_state += ", modified"
        if params.fail_on_first_attempt:
            raise ApplicationError("Failing first attempt")
        return f"global: {global_state}, other module: {stateful_module.some_state}"