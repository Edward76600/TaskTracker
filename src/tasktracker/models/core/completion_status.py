from enum import Enum


class CompletionStatus(str, Enum):
    NOT_STARTED = "Not Started"
    PENDING = "Pending"
    ON_HOLD = "On Hold"
    COMPLETED = "Completed"
