from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_transaction_flow():
    # Create merchant
    client.post("/users/register", json={
        "username": "merchant1",
        "password": "pass",
        "role": "merchant"
    })

    # Create customer
    client.post("/users/register", json={
        "username": "customer1",
        "password": "pass",
        "role": "customer"
    })

    # Login as customer
    login = client.post("/users/login", json={
        "username": "customer1",
        "password": "pass"
    })
    token = login.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Create transaction
    response = client.post("/transactions/", json={
        "merchant_id": 1,   # assumes merchant got ID=1
        "amount": 100.0
    }, headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert "transaction_id" in data
    assert data["status"] in ["SUCCESS", "FAILED"]
