from fastapi.testclient import TestClient
from unittest.mock import patch
from src.main import app

client = TestClient(app)

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to Anomalyze API" in response.json()["message"]

@patch('src.api.routes.collection.insert_one')
def test_ingest_endpoint(mock_insert_one):
    data = {
        "source": "unit-test",
        "timestamp": "2025-03-08T10:00:00Z",
        "data": {"value": 999}
    }
    mock_insert_one.return_value.inserted_id = "mock_id"
    
    response = client.post("/api/ingest", json=data)
    
    assert response.status_code == 200
    assert response.json() == {"message": "Data ingested successfully."}
    mock_insert_one.assert_called_once()
