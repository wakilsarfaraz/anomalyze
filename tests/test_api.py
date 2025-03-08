from fastapi.testclient import TestClient
from unittest.mock import patch
from src.main import app
import pytest
from pymongo import MongoClient
import os

# Set up test client
client = TestClient(app)

# Use the test MongoDB
TEST_MONGO_URI = os.getenv("TEST_MONGO_URI", "mongodb://mongodb-test:27018/anomalyze_test")

@pytest.fixture(scope="module")
def test_db():
    """Creates a test database connection"""
    client = MongoClient(TEST_MONGO_URI)
    db = client.anomalyze_test  # Use isolated test DB
    yield db  # Provide the test DB to tests
    client.drop_database("anomalyze_test")  # Clean up after tests
    client.close()

def test_home_endpoint():
    """Test the home route"""
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome to Anomalyze API" in response.json()["message"]

def test_ingest_endpoint(test_db):
    """Test the ingestion route with the test DB"""
    data = {
        "source": "test-ingest",
        "timestamp": "2025-03-08T10:00:00Z",
        "data": {"value": 999}
    }

    response = client.post("/api/ingest", json=data)
    assert response.status_code == 200
    assert response.json() == {"message": "Data ingested successfully."}

    # Verify data was stored in test DB
    stored_data = test_db.ingestion_data.find_one({"source": "test-ingest"})
    assert stored_data is not None
    assert stored_data["data"]["value"] == 999
