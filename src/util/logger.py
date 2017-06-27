import logging


class Logger(object):

    '''
    Class for logging events such as exception, info or
    debug based on log level
    '''
    def __init__(self):

        self.fmt = "%(asctime)s  %(name)s  %(processName)s  %(filename)s  %(funcName)s \
             %(levelname)s  %(lineno)s  %(module)s  %(threadName)s  \
             %(message)s"

    # Returns logger object for logging
    def logger(self, level='INFO'):
        logger = logging.getLogger()
        handler = logging.StreamHandler()
        # configure logging
        formatter = logging.Formatter(self.fmt)
        handler.setFormatter(fmt=formatter)
        logger.addHandler(handler)
        logger.setLevel(level)
        return logger
