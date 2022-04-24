"""Task Group module."""
from typing import Tuple

from saganSat.models import Task


class TasksGroup:
    """Task Group model."""

    def __init__(self):
        self.tasks = []
        self.payoff = 0
        self.resources = []

    def add_task(self, task: Task):
        """Add a task to the task group."""
        self.tasks.append(task)
        self.payoff += task.payoff
        self.resources.extend(task.resources)

    def add_tasks(self, tasks: Tuple[Task]):
        """Add tasks to the task group."""

        for task in tasks:
            self.add_task(task)
