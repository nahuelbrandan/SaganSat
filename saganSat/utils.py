"""Util functions."""
from typing import List

from saganSat import settings

from saganSat.models import Task


def process_the_tasks_to_group_to_maximize_the_payload(tasks: List[Task]):
    """Process the tasks to group, to maximize the payload.

    Args:
        tasks (List[Task]): list of tasks to group.
    """
    number_of_groups = settings.SATELLITES_QUANTITY
    pass
