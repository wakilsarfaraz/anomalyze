from motor.motor_asyncio import AsyncIOMotorClient
from src.config import settings
import logging

# Logger setup
logger = logging.getLogger(__name__)

# Initialize MongoDB client without immediate connection
client = AsyncIOMotorClient(settings.MONGO_URI, connect=False)
database = client[settings.DATABASE_NAME]

# Collections
anomalies_collection = database.get_collection("anomalies")

async def test_mongo_connection():
    """Test MongoDB connection by inserting a dummy document."""
    try:
        await anomalies_collection.insert_one({"test": "connection"})
        return {"status": "MongoDB is connected"}
    except Exception as e:
        logger.error(f"MongoDB connection failed: {e}")
        return {"status": "MongoDB connection failed", "error": str(e)}

async def close_mongo_connection():
    """Closes the MongoDB connection when the application shuts down."""
    client.close()
    logger.info("MongoDB connection closed successfully.")
