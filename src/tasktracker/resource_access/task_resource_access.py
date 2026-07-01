from tasktracker.resource_access.repository import task_tracker_repository
from tasktracker.models.core.task import Task
from tasktracker.models.host.task_request import TaskRequest


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
