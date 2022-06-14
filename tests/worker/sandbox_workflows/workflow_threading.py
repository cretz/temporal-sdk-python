
print("PRE-IMPORT!!")
import threading
from temporalio import workflow
print("POST-IMPORT!!")

@workflow.defn
class Workflow:
    @workflow.run
    async def run(self) -> None:
        thread = threading.Thread(target=lambda: "<nothing>")
        thread.start()
        thread.join()