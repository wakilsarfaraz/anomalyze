import pytest
from pymongo import MongoClient
from src.main import app
from fastapi.testclient import TestClient
import os

# Determine which MongoDB instance to use (test or production)
MONGO_HOST = os.getenv("MONGO_HOST", "mongodb")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")  # Default is 27017, but will be overridden in test mode

TEST_MODE = os.getenv("TEST_MODE", "false").lower() == "true"

if TEST_MODE:
    MONGO_HOST = "mongodb-test"
    MONGO_PORT = "27018"

MONGO_URI = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/anomalyze"

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
