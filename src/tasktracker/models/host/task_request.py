from pydantic import BaseModel, field_validator
from tasktracker.models.core.completion_status import CompletionStatus


class TaskRequest(BaseModel):
    task_name: str
    completion_status: CompletionStatus

    @field_validator("task_name")
    @classmethod
    def task_name_must_not_be_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("task_name cannot be empty or blank")
        return value.strip()

    @field_validator("completion_status", mode="before")
    @classmethod
    def completion_status_must_be_valid(cls, value: str) -> str:
        valid_values = [status.value for status in CompletionStatus]
        if value not in valid_values:
            raise ValueError(
                f"completion_status must be one of: {', '.join(valid_values)}"
            )
        return value
