import logging

logger = logging.getLogger("test_logger")

def divide(a, b):
	logger.info("dividing " + str(a) + " by " + str(b))
	return a/b