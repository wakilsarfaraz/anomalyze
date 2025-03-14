import requests
import logging
import os
import pymongo
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv("src/config/.env")

# MongoDB connection setup
MONGO_URI = f"mongodb://{os.getenv('MONGO_USER')}:{os.getenv('MONGO_PASS')}@anomalyze-mongodb:27017/anomalyze_db?authSource=admin"
client = pymongo.MongoClient(MONGO_URI)
db = client["anomalyze_db"]
collection = db["temperature_data"]

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def get_coordinates(city_name):
    """Fetch latitude and longitude for a given city from Open-Meteo Geocoding API."""
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        
        if "results" in data and len(data["results"]) > 0:
            city_data = data["results"][0]
            latitude = city_data["latitude"]
            longitude = city_data["longitude"]
            return latitude, longitude
        else:
            logging.error(f"Could not find coordinates for city: {city_name}")
            return None, None

    except requests.exceptions.RequestException as e:
        logging.error(f"Geocoding API request failed: {e}")
        return None, None

def fetch_temperature(city_name):
    """Fetch current temperature for a city and save to MongoDB."""
    latitude, longitude = get_coordinates(city_name)
    
    if latitude is None or longitude is None:
        logging.error(f"Skipping temperature fetch for {city_name} due to missing coordinates.")
        return None

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        temperature = data["current_weather"]["temperature"]
        timestamp = datetime.utcnow().isoformat()

        # Create a record
        record = {
            "timestamp": timestamp,
            "city": city_name,
            "latitude": latitude,
            "longitude": longitude,
            "temperature": temperature
        }

        # Insert into MongoDB
        collection.insert_one(record)

        logging.info(f"Stored in MongoDB: {record}")
        return record

    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
        return None

# Example: Fetch and store temperature for a given city
city = "Dubai"  # Change this to any city name
fetch_temperature(city)
