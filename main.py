"""Main API Rest, to get and process the Tasks."""
import uvicorn
from fastapi import FastAPI

from src import views, settings

app = FastAPI()

# metadata
app.title = settings.TITLE
app.description = settings.DESCRIPTION
app.version = settings.VERSION
app.contact = settings.CONTACT
app.license_info = settings.LICENCE

# endpoints
app.include_router(views.router)


def main():
    """Run server."""

    # TODO creation of processes for the two satellites and perhaps one for the earth station.

    # Run server
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
