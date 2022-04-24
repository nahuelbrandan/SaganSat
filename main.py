"""Main API Rest, to get and process the Tasks."""
import uvicorn
from fastapi import FastAPI

from saganSat import settings, views
from saganSat.satelliteManager import SatellitesManager

satellites_manager = SatellitesManager()


app = FastAPI(
    docs_url=None,
    on_startup=satellites_manager.launch_satellites(),
)

# metadata
app.title = settings.TITLE
app.description = settings.DESCRIPTION
app.version = settings.VERSION
app.contact = settings.CONTACT
app.license_info = settings.LICENCE

# endpoints
app.include_router(views.router)

# satellites
app.satellites_pipes = settings.SATELLITES_PIPES


def main():
    """Run server."""
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
