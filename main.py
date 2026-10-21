import logging

from logger_config import configure_logging
from user_service import register_user, search_user
from database_service import divide_numbers


def main():

    # Configure logging before running application operations.
    configure_logging()

    logger = logging.getLogger(__name__)

    logger.info("Application started.")

    # Demonstrate user registration.
    register_user("varun")

    # Demonstrate user search.
    search_user("admin")

    # Demonstrate exception logging.
    try:
        divide_numbers(10, 0)

    except ZeroDivisionError:
        logger.info(
            "The division exception was handled by the main application."
        )

    # Demonstrate all five logging levels.
    logger.debug("Debug message from the main module.")
    logger.info("Information message from the main module.")
    logger.warning("Warning message from the main module.")
    logger.error("Error message from the main module.")
    logger.critical("Critical message from the main module.")

    logger.info("Application finished.")


if __name__ == "__main__":
    main()