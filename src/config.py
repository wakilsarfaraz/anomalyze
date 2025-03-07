import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    PROJECT_NAME: str = "Anomalyze"
    VERSION: str = "1.0.0"
    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT", 8000))

    # MongoDB Configuration (Using Secure Environment Variables)
    MONGO_USER: str = os.getenv("MONGO_USER")
    MONGO_PASS: str = os.getenv("MONGO_PASS")
    MONGO_HOST: str = os.getenv("MONGO_HOST", "anomalyze-mongo")
    MONGO_PORT: str = os.getenv("MONGO_PORT", "27017")

    # Construct the MongoDB URI securely
    MONGO_URI: str = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/"

    DATABASE_NAME: str = "anomalyze_db"

# Global settings object
settings = Settings()
