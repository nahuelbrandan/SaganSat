"""Satellites Manager."""
from multiprocessing import Process, Pipe

from saganSat import settings
from saganSat.logs import logger
from saganSat.satellites import Satellite


class SatellitesManager:
    """Satellites Manager"""

    def launch_satellites(self):
        """Run the process that works as satellites."""
        satellites_pipes = self._build_satellites()
        settings.SATELLITES_PIPES = satellites_pipes

    @staticmethod
    def land_satellites():
        """Kill the processes that going to works as satellites."""
        for p in settings.SATELLITES_PROCESSES:
            p.terminate()

    @staticmethod
    def get_satellites_names():
        """Get satellites names."""
        satellites_names = [f'Sat-{sat_id}' for sat_id in range(settings.SATELLITES_QUANTITY)]
        return satellites_names

    @staticmethod
    def _build_satellites():
        """Create and run the satellites."""
        logger.info('Creating and running the satellites.')
        satellites_pipes = []
        for i in range(settings.SATELLITES_QUANTITY):
            paren_conn, child_conn = Pipe()
            satellite = Satellite(i, child_conn)
            satellite_process = Process(target=satellite.run, name=satellite.name)
            satellite_process.start()

            settings.SATELLITES_PROCESSES.append(satellite_process)

            satellites_pipes.append(paren_conn)

        return satellites_pipes
