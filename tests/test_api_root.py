"""Test API root endpoint."""
from urllib.parse import urlparse

from fastapi.testclient import TestClient

from main import app
from saganSat import settings

client = TestClient(app)


def test_read_root():
    """Read the root endpoint, that return detail of the system."""
    response = client.get("/")

    assert response.status_code == 200
    assert list(response.json().keys()) == ["title", "description", "version", "docs"]
    assert response.json()['title'] == settings.TITLE
    assert response.json()['version'] == settings.VERSION
    description = "SaganSat, simulate the tasking of a satellites fleet. " \
                  "For more information see the /docs endpoint."
    assert response.json()['description'] == description
    assert urlparse(response.json()['docs']).path == "/docs"


def test_favicon():
    """Get the favicon from endpoint."""
    response = client.get("/favicon.ico")

    assert response.status_code == 200
    assert response.headers['content-type'] == 'image/png'


def test_docs():
    """Get the swagger docs from endpoint."""
    response = client.get("/docs")

    assert response.status_code == 200
    assert response.headers['content-type'] == 'text/html; charset=utf-8'
