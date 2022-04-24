"""Test Configs."""
import pytest

from saganSat.satelliteManager import SatellitesManager


@pytest.fixture(scope="session", autouse=True)
def setup():
    """Run at start the Test Session. Instantiate the server."""
    print('Session Set Up.')
    yield


@pytest.fixture(scope="session", autouse=True)
def teardown():
    """Run at finish the Test Session. Terminate the server."""
    yield
    print('Session Teardown.')
    satellites_manager = SatellitesManager()
    satellites_manager.land_satellites()
