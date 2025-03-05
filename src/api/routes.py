from fastapi import APIRouter
from src.services.database import anomalies_collection

print("Loading API routes...")  # Debugging print

router = APIRouter()

@router.get("/test-mongo")
async def test_mongo():
    """
    API endpoint to verify MongoDB connection.
    """
    try:
        test_doc = {"test": "connection"}
        await anomalies_collection.insert_one(test_doc)
        return {"status": "MongoDB is connected"}
    except Exception as e:
        return {"status": "MongoDB connection failed", "error": str(e)}
