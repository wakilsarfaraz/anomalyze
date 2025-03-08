import pytest
from pymongo import MongoClient
from src.main import app
from fastapi.testclient import TestClient
import os

# Set test database URL
TEST_MONGO_URI = os.getenv("TEST_MONGO_URI", "mongodb://mongodb-test:27018/anomalyze_test")

@pytest.fixture(scope="module")
def test_client():
    """Creates a new TestClient for the FastAPI app"""
    return TestClient(app)

@pytest.fixture(scope="module")
def test_db():
    """Creates a test database connection"""
    client = MongoClient(TEST_MONGO_URI)
    db = client.anomalyze_test  # Use isolated test DB
    yield db  # Provide the test DB to tests
    client.drop_database("anomalyze_test")  # Clean up after tests
    client.close()
