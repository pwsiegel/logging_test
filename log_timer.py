from time import perf_counter

def log_timer(logger):
	def outer(inner):
		start = perf_counter()
		inner()
		end = perf_counter()
		logger.info(inner.__name__ + " ran in " + str((end - start).total_seconds()) + " seconds")

	return outer
