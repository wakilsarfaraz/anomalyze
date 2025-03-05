from motor.motor_asyncio import AsyncIOMotorClient
from src.config import settings

# Initialize MongoDB client
client = AsyncIOMotorClient(settings.MONGO_URI)
database = client[settings.DATABASE_NAME]

# Collections
anomalies_collection = database.get_collection("anomalies")

async def test_mongo_connection():
    try:
        # Check MongoDB connection
        await anomalies_collection.insert_one({"test": "connection"})
        return {"status": "MongoDB is connected"}
    except Exception as e:
        return {"status": "MongoDB connection failed", "error": str(e)}