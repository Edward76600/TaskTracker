import uuid
import datetime as dt
from pydantic import BaseModel, Field
from tasktracker.models.core.completion_status import CompletionStatus


class Task(BaseModel):
    task_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    task_name: str
    completion_status: CompletionStatus
    created_date: dt.date = Field(default_factory=dt.date.today)
    update_date: dt.date = Field(default_factory=dt.date.today)
