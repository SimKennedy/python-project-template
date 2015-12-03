import logging

# Simple print logger

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)-8s - %(message)s')
# logging.debug('This is a log message.')


# Simple file logger
#
# logging.basicConfig(filename='log_filename.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)-8s - %(message)s')
# logging.debug('This is a log message.')


# Print and file logger

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s')

fh = logging.FileHandler('log_filename.txt')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.debug('This is a test log message.')