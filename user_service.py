import logging

logger = logging.getLogger(__name__)


def register_user(username):
    """Simulate registering a user."""

    if not username:
        logger.warning("Registration failed: username is empty.")
        return False

    logger.info("User registration started.")

    # Simulate successful registration.
    logger.info("User registered successfully.")

    return True


def search_user(username):
    """Simulate searching for a user."""

    logger.debug("Searching for user: %s", username)

    if username == "admin":
        logger.info("User found: %s", username)
        return True

    logger.warning("User not found: %s", username)

    return False

