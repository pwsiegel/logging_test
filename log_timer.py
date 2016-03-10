from datetime import datetime

def log_timer(logger):
	def outer(inner):
		start = datetime.now()
		inner()
		end = datetime.now()
		logger.info(inner.__name__ + " ran in " + str((end - start).total_seconds()) + " seconds")

	return outer