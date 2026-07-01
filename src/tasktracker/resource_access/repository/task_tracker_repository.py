import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "tasks.json"


class TaskTrackerRepository:
    def __init__(self) -> None:
        if not DATA_FILE.exists():
            DATA_FILE.write_text("[]")

    def load_data_json(self) -> list:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)

    def save_data_json(self, data: list) -> None:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
