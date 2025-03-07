from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from src.utils.logger import logger  # Ensure logging is applied
import os

print("⚡ DEBUG: routes.py is executing")

# ✅ Explicitly define `router` at the start
router = APIRouter()

# ✅ MongoDB Connection
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017/")
client = MongoClient(MONGO_URI)
db = client["anomalyze"]
collection = db["ingestion_data"]

# ✅ Define Data Model BEFORE Using It
class IngestionRequest(BaseModel):
    source: str
    timestamp: str
    data: dict

# ✅ Force print function list before registering routes
import inspect, sys
print("⚡ DEBUG: Defined functions before attaching to router:", [func[0] for func in inspect.getmembers(sys.modules[__name__], inspect.isfunction)])

# ✅ FORCE REGISTER `/ingest`
@router.post("/ingest", tags=["Ingestion"])
async def ingest_data(request: IngestionRequest):
    """
    API endpoint to ingest structured data into MongoDB.
    """
    print("⚡ DEBUG: /ingest endpoint was called")  # Debugging print
    logger.info("⚡ LOG FILE: /ingest endpoint was hit!")  # Logging
    try:
        logger.info(f"Received data from source: {request.source}")
        collection.insert_one(request.dict())
        logger.info("Data successfully stored in MongoDB.")
        return {"message": "Data ingested successfully."}
    except Exception as e:
        logger.error(f"Error during ingestion: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

# ✅ FORCE REGISTER `/test-mongo`
@router.get("/test-mongo", tags=["Health Check"])
async def test_mongo():
    """
    API endpoint to verify MongoDB connection.
    """
    print("⚡ DEBUG: /test-mongo endpoint was called")  # Debugging print
    try:
        test_doc = {"test": "connection"}
        collection.insert_one(test_doc)
        return {"status": "MongoDB is connected"}
    except Exception as e:
        logger.error(f"MongoDB connection failed: {str(e)}")
        return {"status": "MongoDB connection failed", "error": str(e)}

# ✅ NOW print registered routes AFTER they are attached
print(f"⚡ DEBUG: Final Routes in `routes.py`: {[route.path for route in router.routes]}")
