import logging
import os
from logging.handlers import RotatingFileHandler


# Create the logs directory if it does not exist.
LOG_DIRECTORY = "logs"

os.makedirs(LOG_DIRECTORY, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIRECTORY, "application.log")


# Standard log message format.
LOG_FORMAT = (
    "%(asctime)s - "
    "%(name)s - "
    "%(levelname)s - "
    "%(message)s"
)


def configure_logging():
    """
    Configure application logging.

    DEBUG and higher messages are written to the log file.
    INFO and higher messages are displayed in the terminal.
    """

    # Create a formatter.
    formatter = logging.Formatter(
        fmt=LOG_FORMAT,
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # File handler with log rotation.
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=1024 * 1024,
        backupCount=3,
        encoding="utf-8"
    )

    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Terminal handler.
    console_handler = logging.StreamHandler()

    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Configure the root logger.
    root_logger = logging.getLogger()

    # Avoid adding duplicate handlers if configuration is
    # called more than once.
    if not root_logger.handlers:
        root_logger.setLevel(logging.DEBUG)
        root_logger.addHandler(file_handler)
        root_logger.addHandler(console_handler)
    else:
        # Close handlers only when replacing a configuration
        # is explicitly implemented by the application.
        # Do not silently replace an existing configuration.
        file_handler.close()
        console_handler.close()


if __name__ == "__main__":
    configure_logging()

    logger = logging.getLogger(__name__)

    logger.debug("Debug logging is enabled.")
    logger.info("Logging configuration initialized.")
    logger.warning("This is a sample warning.")
    logger.error("This is a sample error.")
    logger.critical("This is a sample critical message.")