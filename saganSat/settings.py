"""Settings of the system."""
import os

DEBUG = True
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

VERSION = '0.0.1'
TITLE = 'SaganSat'
DESCRIPTION = 'SaganSat, simulate the tasking of a satellites fleet.'
LONG_DESCRIPTION = "TODO SaganSat, simulate the tasking of a satellites fleet."
CONTACT = {
    "name": "Project Support",
    "url": "https://github.com/nahuelbrandan/SaganSat",
    "email": "contact@nahuelbrandan.com",
    "author": "Nahuel Brandán",
}
LICENCE = {
    "name": "GNU GENERAL PUBLIC LICENSE V3",
    "url": "https://www.gnu.org/licenses/gpl-3.0.html"
}

SATELLITES_QUANTITY = 2
SATELLITES_PIPES = None
SATELLITES_PROCESSES = []
SATELLITE_PERCENTAGE_OF_FAILURE = 0.10

LOG_FILENAME = 'logs.log'

LOGO_PATH = os.path.join(BASE_DIR, "resources", "img", "SaganSat_logo.png")
