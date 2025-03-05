import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    PROJECT_NAME: str = "Anomalyze"
    VERSION: str = "1.0.0"
    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT", 8000))

    # MongoDB Configuration
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://anomalyze:secretpassword@anomalyze-mongo:27017/")
    DATABASE_NAME: str = "anomalyze_db"

# Global settings object
settings = Settings()
