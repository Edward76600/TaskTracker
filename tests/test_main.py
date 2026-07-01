from fastapi.testclient import TestClient
from tasktracker.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_tasks():
    response = client.get("/api/v1/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
