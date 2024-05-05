# tests/test_routes.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_user():
    response = client.post(
        "/create_user",
        json={
            "login": "test@example.com",
            "password": "password123",
            "projected": "project_id",
            "env": "prod",
            "domain": "regular"
        }
    )
    assert response.status_code == 200
    assert response.json()["login"] == "test@example.com"


def test_get_users():
    response = client.get("/get_users")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_acquirejock():
    # Assuming you have implemented this endpoint and logic
    response = client.post("/acquirejock", json={"user_id": "69096378-7ffe-4770-8d47-ab8ab43d2809"})
    assert response.status_code == 200
    assert response.json()["message"] == "Lock acquired successfully"


def test_releasejock():
    # Assuming you have implemented this endpoint and logic
    response = client.post("/releasejock", json={"user_id": "69096378-7ffe-4770-8d47-ab8ab43d2809"})
    assert response.status_code == 200
    assert response.json()["message"] == "Lock released successfully"
