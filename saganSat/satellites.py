"""Satellites operations."""
import random
from multiprocessing.connection import Connection

from saganSat.logs import logger


class Satellite:
    """Satellite class."""

    def __init__(self, sat_id: int, connection_pipe: Connection):
        self.id = sat_id
        self.connection_pipe = connection_pipe

    def run(self):
        """Process the tasks that receive."""
        logger.info(f'The satellite {self.id} is successfully on flight. Waiting for tasks to process.')

        while True:
            asd = self.connection_pipe.recv()
            logger.info(f'se encontró un evento nuevo {asd} en el satelite {self.id}')

            operation_result = [self._get_operation_result(x) for x in asd]
            logger.info(operation_result)
            self.connection_pipe.send(operation_result)

    def _get_operation_result(self, x):
        if random.random() < 0.10:
            operation_result = f"The task '{x.name}' was failed, by the Satellite '{self.id}'."
        else:
            operation_result = f"The task '{x.name}' was successfully done, by the Satellite '{self.id}'."

        return operation_result
