import sys
import os
from fastapi.testclient import TestClient
from api.main import app

sys.path.append(os.path.abspath("."))


client = TestClient(app)


def test_homepage():
    response = client.get("/")
    assert response.status_code == 200


def test_homepage_json():
    response = client.get("/")
    assert response.json() == {"message": "API is running"}


def test_docs_page():
    response = client.get("/docs")
    assert response.status_code == 200
