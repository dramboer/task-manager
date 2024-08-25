from task import Task
from typing import List
from datetime import date


class TaskManager:
    def __init__(self):
        """
        Initializes the TaskManager with an empty list of tasks.
        """
        self.tasks: List[Task] = []

    def add_task(self, title: str, description: str, due_date: date):
        """
        Adds a new task to the task list.
        """
        new_task = Task(title, description, due_date)
        self.tasks.append(new_task)

    def get_pending_tasks(self) -> List[Task]:
        """
        Returns a list of tasks that are not yet completed.
        """
        not_completed = []
        for task in self.tasks:
            if not task.completed:
                not_completed.append(task)
        return not_completed

    def get_completed_tasks(self) -> List[Task]:
        """
        Returns a list of tasks that are completed.
        """
        completed = []
        for task in self.tasks:
            if task.completed:
                completed.append(task)
        return completed

    def mark_task_completed(self, task_index: int):
        """
        Marks a specific task as completed based on its index.
        """
        if not task_index < len(self.tasks) or not task_index >= 0:
            return
        self.tasks[task_index].mark_completed()
