from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.utils.logger import logger
from src.api.routes import router
from src.config import settings

# Define an async lifespan function for better logging
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Anomalyze API is starting up...")
    yield  # Application is running
    logger.info("🛑 Anomalyze API is shutting down...")

# Initialize FastAPI app with lifespan
app = FastAPI(title="Anomalyze API", version=settings.VERSION, lifespan=lifespan)

# Enable CORS (Modify allowed origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this for security in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(router, prefix="/api")
logger.info("✅ API routes registered successfully!")

# Debug registered routes using logger
logger.debug(f"🔍 Registered Routes: {[route.path for route in app.routes]}")

# Home route with structured logging
@app.get("/")
async def home():
    logger.info("🏠 Home endpoint accessed.")
    return {"message": "Welcome to Anomalyze API", "version": settings.VERSION}
