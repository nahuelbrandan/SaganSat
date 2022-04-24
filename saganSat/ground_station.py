"""Ground Station class."""
from operator import itemgetter
from typing import List

from saganSat import settings

from saganSat.models import Task


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
                              At most, it will contain N groups, whit N equal a number of Satellites.
        """
        number_of_tasks = len(tasks)

        if number_of_tasks <= settings.SATELLITES_QUANTITY:
            # Case of fewer tasks than satellites
            self.grouped_tasks = [[x] for x in tasks]
        else:
            groups = self._generate_all_posibles_groups(tasks)
            groups = self._sort_groups_by_payoff(groups)
            selected_groups = self._select_groups(groups)
            groups = [x['elems'] for x in selected_groups]

            self.grouped_tasks = groups

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
    def _generate_all_posibles_groups(tasks):
        """
        TODO.
        Args:
            tasks ():

        Returns:

        """
        all_groups = []

        for i in range(len(tasks)):
            tmp = [tasks[i]]
            tmp_payoff = tasks[i].payoff
            tmp_resources = tasks[i].resources

            for j in range(i + 1, len(tasks)):
                if not any(x in tmp_resources for x in tasks[j].resources):
                    tmp.append(tasks[j])
                    tmp_payoff += tasks[j].payoff
                    tmp_resources.extend(tasks[j].resources)

            group = {
                'elems': tmp,
                'payoff': tmp_payoff
            }

            all_groups.append(group)

        return all_groups

    @staticmethod
    def _sort_groups_by_payoff(tasks_grouped):
        """
        TODO.
        Args:
            tasks_grouped ():

        Returns:

        """
        sorted_groups = sorted(tasks_grouped, key=itemgetter('payoff'), reverse=True)

        return sorted_groups

    @staticmethod
    def _select_groups(tasks_grouped):
        """

        Args:
            tasks_grouped ():
        """
        selected_groups = [tasks_grouped[0]]

        for tg in tasks_grouped[1:]:
            if not any(i in tasks_grouped[0]['elems'] for i in tg['elems']):
                selected_groups.append(tg)
                break

        return selected_groups
