"""
    Created by: Baptiste PICARD
    Date: 27/11/2021
    Contact: picard.baptiste22@gmail.com

    Creating a logger base on basicConfig and specific handlers.
"""

# Imports
from logging import (
    getLogger,
    Formatter,
    StreamHandler,
    DEBUG,
    INFO,
    WARNING,
    ERROR
)
from logging.handlers import TimedRotatingFileHandler
# Project modules

# Environment


class HomemadeLogger:
    """ Homemade logger. """
    def __init__(self, name="My Own Logger",
                 level=INFO,
                 log_format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                 handlers=[]):
        """
            Init function.
        """
        if not isinstance(name, str):
            raise TypeError(f"Name must be str instead of {type(name)}.")
        if not isinstance(level, int):
            raise TypeError(f"Level must be str instead of {type(level)}.")
        if not isinstance(log_format, str):
            raise TypeError(f"Log_format must be str instead of {type(log_format)}.")
        if not isinstance(handlers, list):
            raise TypeError(f"Handlers must be list instead of {type(handlers)}.")
        if level not in [DEBUG,
                         INFO,
                         WARNING,
                         ERROR]:
            raise ValueError(f"Level must be in [DEBUG, INFO, WARNING, ERROR] instead of {level}.")
        self.name = (name.strip().lower()
                     .replace(' ', '_'))
        self.level = level
        self.format = log_format
        self.handlers = handlers
        self.create_logger()

    def get_name(self):
        """
        Get the logger name.

        :return: str - Logger name
        """
        return self.name

    def get_level(self):
        """
        Get the logger level.

        :return: int - the logging level
        """
        return self.level

    def get_format(self):
        """
        Get the logger format.

        :return: str - the logging format
        """
        return self.format

    def get_handlers(self):
        """
        Get the logger handlers.

        :return: list
        """
        return self.handlers

    def get_logger(self):
        """
        Get the logger object.

        :return: <Logger> - the logger
        """
        return getLogger(self.get_name())

    def create_logger(self):
        """ Create the logger object using the init config. """
        logger = getLogger(self.get_name())
        logger.setLevel(self.get_level())
        stream_handler = StreamHandler()
        stream_handler.setLevel(self.get_level())
        stream_handler.setFormatter(Formatter(self.get_format()))
        logger.addHandler(stream_handler)
        for handler in self.get_handlers():
            logger.addHandler(handler)

    def log(self,message):
        """ log a message with INFO level. """
        if not isinstance(message, str):
            raise TypeError(f'Message must be str instead of {type(message)}')
        self.get_logger().log(INFO, message)


class HomemadeTimedRotatingFileHandler:
    """ Homemade TimedRotatingFileHandler. """
    def __init__(self, filename='log', when='h', interval=1,
                 log_format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                 level=INFO, log_extension=None, suffix=None):
        """
            Init function.
        """
        if not isinstance(filename, str):
            raise TypeError(f"Filename must be str instead of {type(filename)}.")
        if not isinstance(when, str):
            raise TypeError(f"When must be str instead of {type(when)}.")
        if not isinstance(interval, int):
            raise TypeError(f"Interval must be int instead of {type(interval)}.")
        if not isinstance(log_format, str):
            raise TypeError(f"log_format must be str instead of {type(log_format)}.")
        if not isinstance(level, int):
            raise TypeError(f"Level must be str instead of {type(level)}.")
        if log_extension and not isinstance(log_extension, str):
            raise TypeError(f"log_file_name must be str instead of {type(log_extension)}.")
        if suffix and not isinstance(suffix, str):
            raise TypeError(f"Suffix must be str instead of {type(suffix)}.")
        if level not in [DEBUG,
                         INFO,
                         WARNING,
                         ERROR]:
            raise ValueError(f"Level must be in [DEBUG, INFO, WARNING, ERROR] instead of {level}.")
        if when.upper() not in ['S', 'M', 'H', 'D',
                                'W0', 'W1', 'W2', 'W3',
                                'W4', 'W5', 'W6', 'MIDNIGHT']:
            raise ValueError("Bad value for when.")
        if interval < 1:
            raise ValueError("Interval must be >=1")
        self.filename = filename
        self.when = when.upper()
        self.interval = interval
        self.format = log_format
        self.level = level
        self.log_extension = log_extension
        self.suffix = suffix
        self.handler = self.build_handler()

    def get_filename(self):
        """
        Get the handler filename.

        :return: str
        """
        return self.filename

    def get_when(self):
        """
        Get handler when item.

        :return: str
        """
        return self.when

    def get_interval(self):
        """
        Get the handler interval.

        :return: int
        """
        return self.interval

    def get_format(self):
        """
        Get the handler format.

        :return: str - the handler format
        """
        return self.format

    def get_level(self):
        """
        Get the handler level.

        :return: int - the handler level
        """
        return self.level

    def get_log_extension(self):
        """
        Get the handler file_extension.

        :return: int
        """
        return self.log_extension

    def get_suffix(self):
        """
        Get the handler suffix.

        :return: str
        """
        return self.suffix

    def get_handler(self):
        """
        Get the TimedRotatingFileHandler object.

        :return: logging handler
        """
        return self.handler

    def build_handler(self):
        handler = TimedRotatingFileHandler(filename=self.get_filename(),
                                           when=self.get_when(),
                                           interval=self.get_interval())
        handler.setLevel(self.get_level())
        handler.setFormatter(Formatter(self.get_format()))
        if self.get_log_extension():
            handler.namer = lambda name: name + self.get_log_extension()
        if self.get_suffix():
            handler.suffix = self.get_suffix()
        return handler
