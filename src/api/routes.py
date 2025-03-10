from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from pymongo import MongoClient
from src.utils.logger import logger  # Ensure logging is applied
import os
from urllib.parse import quote_plus

# ✅ Explicitly define `router` at the start
router = APIRouter()

# ✅ Read environment variables
TEST_MODE = os.getenv("TEST_MODE", "false").lower() == "true"

MONGO_HOST = os.getenv("MONGO_HOST", "mongodb")
MONGO_TEST_HOST = os.getenv("MONGO_TEST_HOST", "mongodb-test")  # Ensure this is set if using a separate test DB

MONGO_PORT = os.getenv("MONGO_PORT", "27017")
MONGO_TEST_PORT = os.getenv("MONGO_TEST_PORT", "27017")  # Default to 27017 unless intentionally changed

MONGO_USER = os.getenv("MONGO_USER", "")
MONGO_PASS = os.getenv("MONGO_PASS", "")

# ✅ Ensure MongoDB credentials are URL-safe
MONGO_USER_ENCODED = quote_plus(MONGO_USER)
MONGO_PASS_ENCODED = quote_plus(MONGO_PASS)

# ✅ Define the MongoDB connection string with authentication
MONGO_URI_TEMPLATE = "mongodb://{user}:{password}@{host}:{port}/"

if TEST_MODE:
    MONGO_URI = MONGO_URI_TEMPLATE.format(
        user=MONGO_USER_ENCODED, password=MONGO_PASS_ENCODED,
        host=MONGO_TEST_HOST, port=MONGO_TEST_PORT
    )
else:
    MONGO_URI = MONGO_URI_TEMPLATE.format(
        user=MONGO_USER_ENCODED, password=MONGO_PASS_ENCODED,
        host=MONGO_HOST, port=MONGO_PORT
    )

# ✅ Dependency for MongoDB Connection
def get_mongo_client():
    return MongoClient(MONGO_URI)

# ✅ Define Data Model
class IngestionRequest(BaseModel):
    source: str
    timestamp: str
    data: dict

# ✅ Define Response Model
class IngestionResponse(BaseModel):
    message: str

class HealthCheckResponse(BaseModel):
    status: str
    error: str | None = None

# ✅ `/ingest` Route with Proper Logging
@router.post("/ingest", tags=["Ingestion"], response_model=IngestionResponse)
async def ingest_data(request: IngestionRequest, client: MongoClient = Depends(get_mongo_client)):
    """
    API endpoint to ingest structured data into MongoDB.
    """
    logger.debug("Processing /ingest request")  # Debug logging
    try:
        logger.info(f"Received data from source: {request.source}")
        db = client["anomalyze_test" if TEST_MODE else "anomalyze"]
        collection = db["ingestion_data"]
        collection.insert_one(request.model_dump())  # ✅ Fixed `.dict()` -> `.model_dump()`
        logger.info("Data successfully stored in MongoDB.")
        return {"message": "Data ingested successfully."}
    except Exception as e:
        logger.error(f"Error during ingestion: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# ✅ `/test-mongo` Route with Dependency Injection
@router.get("/test-mongo", tags=["Health Check"], response_model=HealthCheckResponse)
async def test_mongo(client: MongoClient = Depends(get_mongo_client)):
    """
    API endpoint to verify MongoDB connection.
    """
    logger.debug("Processing /test-mongo request")  # Debug logging
    try:
        db = client["anomalyze_test" if TEST_MODE else "anomalyze"]
        collection = db["ingestion_data"]
        test_doc = {"test": "connection"}
        collection.insert_one(test_doc)
        return {"status": "MongoDB is connected", "error": None}
    except Exception as e:
        logger.error(f"MongoDB connection failed: {str(e)}")
        return {"status": "MongoDB connection failed", "error": str(e)}
