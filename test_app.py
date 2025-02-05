# test_app.py
import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_check(client):
    rv = client.get("/health")
    assert rv.status_code == 200
    assert rv.json["status"] == "healthy"


def test_add_task(client):
    rv = client.post("/add_task", data={"title": "Test Task"})
    assert rv.status_code == 302  # Redirect after successful post
