from fastapi import FastAPI
from src.database import get_db_connection

app = FastAPI()

@app.get("/")
async def root():
    try:
        conn = get_db_connection()
        conn.close()
        return {"message": "Connected to PostgreSQL successfully!"}
    except Exception as e:
        return {"error": str(e)}
