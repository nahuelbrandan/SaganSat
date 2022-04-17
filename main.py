# !/usr/bin/env python
"""Main API Rest, to get and process the Tasks."""
import uvicorn
from fastapi import FastAPI

from saganSat import settings, views
from multiprocessing import Process, Pipe

from saganSat.satellites import Satellite

app = FastAPI()

# metadata
app.title = settings.TITLE
app.description = settings.DESCRIPTION
app.version = settings.VERSION
app.contact = settings.CONTACT
app.license_info = settings.LICENCE

# endpoints
app.include_router(views.router)


def build_satellites():
    """Create and run the satellites."""
    satellites_pipes = []
    for i in range(settings.SATELLITES_QUANTITY):
        paren_conn, child_conn = Pipe()
        satellite = Satellite(i, child_conn)
        satellite_process = Process(target=satellite.run)
        satellite_process.start()

        satellites_pipes.append(paren_conn)

    return satellites_pipes


def main():
    """Run server."""

    satellites_pipes = build_satellites()
    app.satellites_pipes = satellites_pipes

    # Run server
    # noinspection PyTypeChecker
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
