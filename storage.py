# JSON file storage module
import json
import os
from task import Task

DATA_FILE = "data.json"


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            return [Task.from_dict(item) for item in data]
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            [task.to_dict() for task in tasks],
            file,
            ensure_ascii=False,
            indent=4
        )