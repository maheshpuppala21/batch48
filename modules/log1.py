import logging
logging.basicConfig(level=logging.DEBUG, #for filtering the log statements
	format="%(asctime)s-->%(levelname)s==>%(message)s",filename="log.txt")
logging.info("INFO Message")
logging.error("error Message")
logging.warn("warning Message")
logging.debug("debug Message")
