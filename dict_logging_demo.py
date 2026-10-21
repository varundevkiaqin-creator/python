import json
import logging
import logging.config
import os


os.makedirs("logs", exist_ok=True)

with open("logging_config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

logger.debug("Debug message")
logger.info("Application started")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
