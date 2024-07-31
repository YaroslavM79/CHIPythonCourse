import logging

__all__ = ['Logger']

LOG_LEVEL = {
    'critical': (logging.CRITICAL, '%(asctime)s %(levelname)-8s [%(name)s] %(message)s'),
    'error': (logging.ERROR, '%(asctime)s %(levelname)-8s [%(name)s] %(message)s'),
    'warning': (logging.WARNING, '%(asctime)s %(levelname)-8s [%(name)s] %(message)s'),
    'info': (logging.INFO, '%(asctime)s %(levelname)-8s [%(name)s] %(message)s'),
    'debug': (logging.DEBUG, '%(pathname)s:%(lineno)d:\n%(asctime)s %(levelname)-8s [%(name)s] %(message)s'),
    'notset': (logging.NOTSET, '%(asctime)s %(levelname)-8s [%(name)s] %(message)s')
}


class Logger:

    def __init__(self, log_level):
        self._datefmt = "%d-%m-%Y:%H:%M:%S"
        self.log_level = self._get_log_level(log_level)
        self.log_format = self._get_log_format(log_level)
        self._config()
        self._loggers = []
        self._loggers.append("app.py info")

    def _get_log_level(self, log_level):
        return LOG_LEVEL[log_level][0]

    def _get_log_format(self, log_level):
        return LOG_LEVEL[log_level][1]

    def _config(self):
        """
        Basic logging config.
        """
        logging.basicConfig(
            format=self.log_format,
            datefmt=self._datefmt,
            level=self.log_level)

    def update_loggers(self, loggers):
        if loggers:
            self._loggers.extend(loggers.split(","))
        for logger in self._loggers:
            name, level = logger.split()
            self._update_logger_level(name.strip(), level.strip())

    def _update_logger_level(self, log_name: str, log_level: str):
        """
        Update logging level and format for certain logger.
        :param log_name:
        :param log_level:
        :return:
        """
        logging_level = self._get_log_level(log_level)
        logging_format = self._get_log_format(log_level)

        logger = logging.getLogger(log_name)
        logger.propagate = False

        handler = logging.StreamHandler()

        formatter = logging.Formatter(logging_format, datefmt=self._datefmt)
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.setLevel(logging_level)
