# task_agent.py

import json
from datetime import datetime
from pathlib import Path

tasks_file = Path("app/data/tasks.json")

def load_tasks():
    if not tasks_file.exists():
        return []
    with open(tasks_file, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(tasks_file, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(user_task: str):
    tasks = load_tasks()
    task_entry = {
        "task": user_task,
        "timestamp": datetime.now().isoformat()
    }
    tasks.append(task_entry)
    save_tasks(tasks)
    return task_entry

def get_all_tasks():
    return load_tasks()

def delete_task(index: int):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        return removed
    return None
