import logging
import os

# Define log file path
LOG_FILE = "/workspace/anomalyze.log"  # Ensure it's in the correct directory

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),  # Logs to a file
        logging.StreamHandler()  # Logs to console
    ]
)

logger = logging.getLogger(__name__)


