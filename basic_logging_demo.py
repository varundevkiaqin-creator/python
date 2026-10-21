import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="basic_logging.log",
    filemode="a",
    encoding="utf-8",
    force=True
)

logger = logging.getLogger(__name__)

logger.debug("Debug message")
logger.info("Application started")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")