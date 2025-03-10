import os
from dotenv import load_dotenv
from urllib.parse import quote_plus
from pydantic_settings import BaseSettings


# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Anomalyze"
    VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1")

    # Server Configuration
    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT", 8000))

    # MongoDB Configuration (Using Secure Encoding)
    MONGO_USER: str = os.getenv("MONGO_USER", "")
    MONGO_PASS: str = os.getenv("MONGO_PASS", "")
    MONGO_HOST: str = os.getenv("MONGO_HOST", "anomalyze-mongo")
    MONGO_PORT: str = os.getenv("MONGO_PORT", "27017")
    
    # URL-encoded credentials for MongoDB connection
    MONGO_USER_ENCODED: str = quote_plus(MONGO_USER)
    MONGO_PASS_ENCODED: str = quote_plus(MONGO_PASS)
    MONGO_URI: str = f"mongodb://{MONGO_USER_ENCODED}:{MONGO_PASS_ENCODED}@{MONGO_HOST}:{MONGO_PORT}/"

    DATABASE_NAME: str = "anomalyze_db"

# Global settings object
settings = Settings()
