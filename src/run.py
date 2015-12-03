import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)-8s - %(message)s')


def function():
    logging.debug('test')


if __name__ == '__main__':
    function()