from fastapi import APIRouter
from tasktracker.models.core.completion_status import CompletionStatus
from tasktracker.models.host.task_request import TaskRequest
from tasktracker.models.core.task import Task
from tasktracker.resource_access.task_resource_access import TaskResourceAccess

router = APIRouter()
task_resource_access = TaskResourceAccess()


@router.get("/tasks", tags=["tasks"])
def list_tasks() -> list[Task]:
    return task_resource_access.get_all_tasks()


@router.post("/tasks", tags=["tasks"], status_code=201)
def create_task(task: TaskRequest) -> Task:
    return task_resource_access.add_task(task)


@router.delete("/tasks/{task_id}", tags=["tasks"], status_code=204)
def delete_task(task_id: str) -> None:
    task_resource_access.delete_task(task_id)

@router.put("/tasks/{task_id}", tags=["tasks"], status_code=200)
def update_task(task_id: str, status: CompletionStatus) -> Task:
    return task_resource_access.update_task(task_id, status)
