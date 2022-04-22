"""Test API request.

This tests works as an integration tests.
"""
from urllib.parse import urlparse

from fastapi.testclient import TestClient
from saganSat import settings

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")

    assert response.status_code == 200
    assert list(response.json().keys()) == ["title", "description", "version", "docs"]
    assert response.json()['title'] == settings.TITLE
    assert response.json()['version'] == settings.VERSION
    description = "SaganSat, simulate the tasking of a satellites fleet. " \
                  "For more information see the /docs endpoint."
    assert response.json()['description'] == description
    assert urlparse(response.json()['docs']).path == "/docs"
