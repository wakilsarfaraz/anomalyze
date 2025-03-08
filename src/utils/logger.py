import logging
from pathlib import Path
import os

log_file_path = Path(os.getenv("LOG_FILE_PATH", "anomalyze.log"))

# Ensure the parent directory exists
log_file_path.parent.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("anomalyze")
logger.setLevel(logging.INFO)

if not logger.handlers:
    logger.addHandler(logging.FileHandler(log_file_path))
    logger.addHandler(logging.StreamHandler())

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
for handler in logger.handlers:
    handler.setFormatter(formatter)
