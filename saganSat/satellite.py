"""Satellite class."""
from multiprocessing.connection import Connection
from random import random

from saganSat import settings
from saganSat.logs import logger


class Satellite:
    """Satellite class.

    This class represent a Satellite in flight.
    That could receive tasks to perform and return its result.
    """

    def __init__(self, sat_id: int, connection_pipe: Connection):
        self.id = sat_id
        self.name = f'Sat-{sat_id}'
        self.connection_pipe = connection_pipe

    def run(self):
        """Process The tasks that receive."""
        logger.info(f'The satellite {self.name} is successfully on flight. Waiting for tasks to process.')

        while True:
            tasks = self.connection_pipe.recv()
            logger.info(f'A new tasks was received in the satellite {self.name}. Tasks: {tasks}')

            operation_result = [self._get_operation_result(x.name) for x in tasks]
            logger.info(f'Operation result: {operation_result}')

            self.connection_pipe.send(operation_result)

    def _get_operation_result(self, task_name: str):
        """Simulate an operation execution. Returning the operation result."""
        if random() < settings.SATELLITE_PERCENTAGE_OF_FAILURE:
            operation_result = f"The task '{task_name}' was failed, by the Satellite {self.name}."
        else:
            operation_result = f"The task '{task_name}' was successful, by the Satellite {self.name}."

        return operation_result
