import logging

logger = logging.getLogger(__name__)


def divide_numbers(a, b):
    """
    Demonstrate exception logging.

    This function intentionally allows the division
    error to propagate to its caller.
    """

    logger.info("Division operation started.")

    try:
        result = a / b

    except ZeroDivisionError:
        logger.exception("Division failed because the divisor was zero.")
        raise

    logger.info("Division operation completed successfully.")

    return result


