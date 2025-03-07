import sys
import os
from fastapi import FastAPI
from src.utils.logger import logger  # Import the logger
from src.api.routes import router  # Ensure the "src.api.routes" path is correct
from src.config import settings

# Ensure the correct import path for modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Initialize FastAPI app
logger.info("Starting Anomalyze API...")
app = FastAPI(title="Anomalyze API", version=settings.VERSION)

# Register API routes
logger.info("Registering API routes...")
app.include_router(router, prefix="/api")  # ✅ Corrected: Now attaching the router
logger.info("Routes registered successfully!")

# Debug registered routes (AFTER they are attached)
print(f"⚡ DEBUG: Registered Routes: {[route.path for route in app.routes]}")

# Home route with logging
@app.get("/")
def home():
    print("⚡ DEBUG: Home endpoint was hit!")  # Print to console
    logger.info("⚡ LOG FILE: Home endpoint accessed!")  # Log to file
    return {"message": "Welcome to Anomalyze API", "version": settings.VERSION}
