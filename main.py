import logging

# https://docs.python.org/3/library/logging.html#record-attributes

logging.basicConfig(level=logging.INFO, filename="log.log", filemode="w")

logging.info("info")
logging.debug("debug")
logging.warning("warning")
logging.error("error")
logging.critical("critical")


'''
example output


WARNING:root:warning
ERROR:root:error
CRITICAL:root:critical
'''