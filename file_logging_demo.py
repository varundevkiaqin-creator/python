import logging
import logging.config
import os


os.makedirs("logs", exist_ok=True)

logging.config.fileConfig(
    "logging.ini",
    disable_existing_loggers=False
)

logger = logging.getLogger(__name__)

logger.debug("Debug message")
logger.info("Application started")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")