import logging


class ErrorOnlyFilter(logging.Filter):

    def filter(self, record):
        return record.levelno >= logging.ERROR


logger = logging.getLogger("filter_demo")
logger.setLevel(logging.DEBUG)
logger.propagate = False

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

handler.addFilter(ErrorOnlyFilter())

formatter = logging.Formatter(
    "%(levelname)s - %(message)s"
)

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug("This debug message will be filtered out.")
logger.info("This info message will be filtered out.")
logger.warning("This warning message will be filtered out.")

logger.error("This error message will be displayed.")
logger.critical("This critical message will be displayed.")
