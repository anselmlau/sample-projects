import logging


class Logger(object):

    logging.basicConfig(filename='log.txt')

    def __init__(self):
        pass

    @staticmethod
    def log_info(cls=None, msg=None):

        logging.getLogger(cls).info(msg)

    @staticmethod
    def log_warn(cls=None, msg=None):

        logging.getLogger(cls).warn(msg)

    @staticmethod
    def log_error(cls=None, msg=None):

        logging.getLogger(cls).error(msg)

