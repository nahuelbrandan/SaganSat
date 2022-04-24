"""Satellites operations."""
import random
from multiprocessing.connection import Connection

from saganSat.logs import logger


class Satellite:
    """Satellite class."""

    def __init__(self, sat_id: int, connection_pipe: Connection):
        self.id = sat_id
        self.name = f'Sat-{sat_id}'
        self.connection_pipe = connection_pipe

    def run(self):
        """Process the tasks that receive."""
        logger.info(f'The satellite {self.name} is successfully on flight. Waiting for tasks to process.')

        while True:
            task = self.connection_pipe.recv()
            logger.info(f'A new task was received in the satellite {self.name}. Task: {task}')

            operation_result = [self._get_operation_result(x) for x in task]
            logger.info(f'Operation result: {operation_result}')

            self.connection_pipe.send(operation_result)

    def _get_operation_result(self, x):
        if random.random() < 0.10:
            operation_result = f"The task '{x.name}' was failed, by the Satellite {self.name}."
        else:
            operation_result = f"The task '{x.name}' was successfully, by the Satellite {self.name}."

        return operation_result
