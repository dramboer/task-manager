from datetime import date


class Task:
    def __init__(self, title: str, description: str, due_date: date):
        """
        Initializes a new task with a title, description, and due date.
        """
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_completed(self):
        """
        Marks the task as completed.

        """
        self.completed = True

    def __str__(self):
        """
        Returns a string representation of the task.

        """

        status_string = ""
        if self.completed:
            status_string = "Completed"
        else:
            status_string = "In Progress"

        return f"{self.title}\n{self.description}\n{self.due_date}\n{status_string}"
