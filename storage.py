
import json
from pathlib import Path

FILE_PATH = Path(__file__).parent / "students.json"


def load_students():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_students(students):
    with open(FILE_PATH, "w") as file:
        json.dump(students, file, indent=4)
