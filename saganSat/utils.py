"""Util functions."""
from operator import itemgetter
from typing import List

from saganSat import settings

from saganSat.models import Task


def generate_all_posibles_groups(tasks):
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


def sort_groups_by_payoff(tasks_grouped):
    """
    TODO.
    Args:
        tasks_grouped ():

    Returns:

    """
    sorted_groups = sorted(tasks_grouped, key=itemgetter('payoff'), reverse=True)

    return sorted_groups


def select_groups(tasks_grouped, number_of_tasks):
    """

    Args:
        tasks_grouped ():
        number_of_tasks ():
    """
    # case all tasks are in a same group
    if len(tasks_grouped[0]) == number_of_tasks:
        return [tasks_grouped[0]]

    selected_groups = [tasks_grouped[0]]

    for tg in tasks_grouped[1:]:
        if not any(i in tasks_grouped[0]['elems'] for i in tg['elems']):
            selected_groups.append(tg)
            break

    return selected_groups


def group_tasks_to_run_per_satellite(tasks: List[Task]):
    """Group the tasks to be run per Satellite, taking into account the constraints.

    Args:
        tasks (List[Task]): list of tasks to group.

    Returns:
        List[List[Task]]: list of tasks grouped.
                          At most, it will contain N groups, whit N equal a number of Satellites.
    """
    number_of_groups = settings.SATELLITES_QUANTITY
    number_of_tasks = len(tasks)

    # Case of fewer tasks than satellites
    if number_of_tasks <= number_of_groups:
        return [[x] for x in tasks]

    tasks_grouped = generate_all_posibles_groups(tasks)
    tasks_grouped = sort_groups_by_payoff(tasks_grouped)
    tasks_selected = select_groups(tasks_grouped, number_of_tasks)

    response = [x['elems'] for x in tasks_selected]
    return response
