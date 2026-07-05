import datetime as dt

from tasktracker.models.core.completion_status import CompletionStatus
from tasktracker.models.core.task import Task
from tasktracker.models.host.task_request import TaskRequest
from tasktracker.resource_access.repository import task_tracker_repository


class TaskResourceAccess:
    def __init__(self) -> None:
        self.repo = task_tracker_repository.TaskTrackerRepository()

    def get_all_tasks(self) -> list[Task]:
        data = self.repo.load_data_json()
        return [Task.model_validate(item) for item in data]

    def add_task(self, request: TaskRequest) -> Task:
        task = Task(
            task_name=request.task_name,
            completion_status=request.completion_status,
        )
        data = self.repo.load_data_json()
        data.append(task.model_dump(mode="json"))
        self.repo.save_data_json(data)
        return task

    def delete_task(self, task_id: str) -> None:
        data = self.repo.load_data_json()
        data = [t for t in data if t["task_id"] != task_id]
        self.repo.save_data_json(data)

    def update_task(self, task_id: str, status: CompletionStatus) -> Task:
        data = self.repo.load_data_json()
        updated_task = next((t for t in data if t["task_id"] == task_id), None)
        if updated_task is None:
            raise ValueError(f"Task {task_id} not found")
        updated_task["completion_status"] = status.value
        updated_task["update_date"] = dt.date.today().isoformat()
        self.repo.save_data_json(data)
        return Task.model_validate(updated_task)
