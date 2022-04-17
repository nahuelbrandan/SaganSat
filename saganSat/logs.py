"""Logs manager."""
import logging
import sys

from saganSat import settings

logger = logging.getLogger()
level = logging.DEBUG if settings.DEBUG else logging.INFO
logger.setLevel(level)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', '%Y-%m-%d %H:%M:%S')

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(level)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler(settings.LOG_FILENAME)
file_handler.setLevel(level)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)
