from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_and_login():
    # Register a user
    response = client.post("/users/register", json={
        "username": "testuser",
        "password": "testpass",
        "role": "customer"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "User registered successfully"

    # Login with the same user
    response = client.post("/users/login", json={
        "username": "testuser",
        "password": "testpass"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
