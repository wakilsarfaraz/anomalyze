from fastapi import FastAPI
from src.api.routes import router
from src.config import settings

# Initialize FastAPI app
app = FastAPI(title="Anomalyze API", version=settings.VERSION)

# Register API routes
app.include_router(router)

@app.get("/")
def home():
    """
    Root endpoint to check API status.
    """
    return {"message": "Welcome to Anomalyze API", "version": settings.VERSION}
