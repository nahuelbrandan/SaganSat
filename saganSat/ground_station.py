"""Ground Station module."""
from itertools import islice
from typing import List

from saganSat import settings
from saganSat.models import Task
from saganSat.task_group import TasksGroup


class GroundStation:
    """Ground Station class.

    This class represent a Ground Station.
    That could receive tasks to administrate and send to the satellites.
    """
    def __init__(self, satellites_pipes):
        self.satellites_pipes = satellites_pipes
        self.grouped_tasks = []

    def group_tasks_to_run_per_satellite(self, tasks: List[Task]):
        """Group the tasks to be run per Satellite, taking into account the constraints.

        Args:
            tasks (List[Task]): list of tasks to group.

        Returns:
            List[List[Task]]: list of tasks grouped.
                              At most, it will contain N task_groups, whit N equal a number of Satellites.
        """
        if len(tasks) <= settings.SATELLITES_QUANTITY:
            # Case of fewer tasks than satellites, run one task per satellite
            self.grouped_tasks = [[x] for x in tasks]
        else:
            task_groups = self._generate_all_posibles_task_groups(tasks)
            task_groups.sort(key=lambda x: x.payoff, reverse=True)  # sort by payoff
            selected_task_groups = self._select_task_groups(task_groups)
            task_groups = [x.tasks for x in selected_task_groups]

            self.grouped_tasks = task_groups

    def send_grouped_tasks_to_the_satellites(self):
        """Send the grouped tasks by Pipes, to the satellites, to be executed by them."""
        for i, tg in enumerate(self.grouped_tasks):
            self.satellites_pipes[i].send(self.grouped_tasks[i])

    def get_responses_of_satellites(self):
        """Obtain the result of the execution of the tasks by the satellites.

        Returns:
            List[str]: list of results, for each task the satellites received.
        """
        responses_from_satellites = []
        for i, _ in enumerate(self.grouped_tasks):
            responses_from_satellites.extend(self.satellites_pipes[i].recv())

        return responses_from_satellites

    @staticmethod
    def _generate_all_posibles_task_groups(tasks: List[Task]) -> List[TasksGroup]:
        """Generate all posibles tasks task_groups, taking into account the constraints.

        Args:
            tasks (List[Task]): list of Tasks to be grouped.

        Returns:
            List[TasksGroup]: list of Tasks grouped.
        """
        all_groups = []

        for i, t in enumerate(tasks):
            task_group = TasksGroup()
            task_group.add_task(t)

            for u in islice(tasks, i + 1, len(tasks)):
                # if not have resources in common
                if not any(x in task_group.resources for x in u.resources):
                    task_group.add_task(u)

            all_groups.append(task_group)

        return all_groups

    @staticmethod
    def _select_task_groups(tasks_groups: List[TasksGroup]) -> List[TasksGroup]:
        """From list of tasks groups, select those indicated to be executed by the satellites.

        Args:
            tasks_groups (List[TasksGroup]): list of all tasks groups available.

        Returns:
            List[TasksGroup]: selected tasks groups.
        """
        # add the better tasks group
        selected_groups = [tasks_groups[0]]

        # search for the next task group
        for tg in tasks_groups[1:]:
            if not any(i in tasks_groups[0].tasks for i in tg.tasks):
                selected_groups.append(tg)
                break

        return selected_groups
