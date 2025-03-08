from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to Anomalyze API",
        "version": "1.0.0"
    }

def test_ingest_endpoint():
    data = {
        "source": "unit-test",
        "timestamp": "2025-03-08T10:00:00Z",
        "data": {"value": 999}
    }
    response = client.post("/api/ingest", json=data)
    assert response.status_code == 200
    assert response.json()["message"] == "Data ingested successfully."
