import logging
import sys
from module import divide
from s3handler import S3Handler
from log_timer import log_timer

#Set up the logger with an S3 handler
logger = logging.getLogger("test_logger")
handler = S3Handler("my_bucket", "log.txt")
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

#Sets up logging for uncaught exceptions
def uncaught_error(exc_type, exc_value, exc_traceback):
	logger.error("Uncaught Exception", exc_info = (exc_type, exc_value, exc_traceback))
	sys.__excepthook__(exc_type, exc_value, exc_traceback)
	return

sys.excepthook = uncaught_error

if __name__ == '__main__':
	#Normal logging behavior
	logger.info("first division problem")
	print(divide(5,2))
	
	#Use a decorator to 
	@log_timer(logger)
	def long_task():
		num = 0

		for i in range(0,100000):
			num += 2**(-i)

		print(num)

	#Trigger an uncaught exception
	logger.info("second division problem")
	print(divide(10,0))