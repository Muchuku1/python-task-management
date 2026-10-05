from datetime import datetime

# Import validation functions
from validation import *

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)

    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)


    print("Task added successfully!")
    
# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    def mark_task_as_complete(index, tasks=tasks):
        if index < 0 or index >= len(tasks):
            print("Invalid task number.")
            return

    tasks[index]["completed"] = True
    print("Task marked as complete!")
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    def view_pending_tasks(tasks=tasks):
        pending_tasks = [
            task for task in tasks
            if not task["completed"]
        ]

    if not pending_tasks:
        print("No pending tasks.")
        return

    print("\nPending Tasks:")

    for index, task in enumerate(tasks):
        if not task["completed"]:
            print(f"\nTask {index + 1}")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        return 0

    completed_tasks = sum(
        1 for task in tasks
        if task["completed"]
    )

    progress = (completed_tasks / len(tasks)) * 100

    return progress
    