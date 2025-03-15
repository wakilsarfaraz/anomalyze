import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set to DEBUG for more details
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("anomalyze.log"),  # Log to a file
        logging.StreamHandler()  # Log to console
    ]
)

# Create logger instance
logger = logging.getLogger("anomalyze")
