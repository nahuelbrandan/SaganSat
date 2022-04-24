"""Test Satellite class."""
from multiprocessing import Pipe

from saganSat.satellite import Satellite


class TestSatellite:

    def test_init(self):
        sat_id = 5
        _, conn = Pipe()
        satellite = Satellite(
            sat_id=sat_id,
            connection_pipe=conn
        )

        assert satellite.id == sat_id
        assert satellite.name == f'Sat-{sat_id}'
        assert satellite.connection_pipe == conn

    def test_get_operation_result(self):
        sat_id = 5
        _, conn = Pipe()
        satellite = Satellite(
            sat_id=sat_id,
            connection_pipe=conn
        )

        task_name = 'take pictures'
        posible_responses = [
            f"The task '{task_name}' was successful, by the Satellite Sat-5.",
            f"The task '{task_name}' was failed, by the Satellite Sat-5."
        ]
        assert satellite._get_operation_result(task_name) in posible_responses
