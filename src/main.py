import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # Ensure correct import path

from fastapi import FastAPI
from src.api.routes import router  # <== Ensure the "src.api.routes" path is correct
from src.config import settings

print("Loading FastAPI...")  # Debugging print

# Initialize FastAPI app
app = FastAPI(title="Anomalyze API", version=settings.VERSION)

print("Registering API routes...")  # Debugging print
app.include_router(router, prefix="/api")
print("Routes registered successfully!")  # Debugging print

@app.get("/")
def home():
    return {"message": "Welcome to Anomalyze API", "version": settings.VERSION}
