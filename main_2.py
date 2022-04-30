import logging

# high level
format_logging = logging.getLogger(__name__)

# set log file handler
sample_log_file_handler = logging.FileHandler(filename='sample_log_file.log', mode='w')

# set the log level
format_logging.setLevel(logging.DEBUG)

# set log formatter 
sample_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
sample_log_file_handler.setFormatter(sample_log_formatter)

# set file handler
format_logging.addHandler(sample_log_file_handler)

format_logging.info("info")
format_logging.info("info2")
format_logging.debug("debug")

'''
2022-04-30 19:35:41,162 - __main__ - INFO - info
2022-04-30 19:35:41,162 - __main__ - INFO - info2
2022-04-30 19:35:41,162 - __main__ - DEBUG - debug
'''