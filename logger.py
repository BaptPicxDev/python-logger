"""
    Created by: Baptiste PICARD
    Date: 27/11/2021
    Contact: picard.baptiste22@gmail.com

    Creating a logger
"""

## Imports
from logging import (
    basicConfig,
    DEBUG,
    INFO,
    WARNING,
    ERROR
)
## Project modules

## Environment

## Functions

## Classes
class Logger:
    """
        Homemade logger.
    """

    def __init__(self, name="My Own Logger",
                 level=INFO,
                 log_format="%(asctime)s %(message)s"):
        """
            Init function.
        """
        if not isinstance(name, str):
            raise TypeError("Name must be str.")
        if not isinstance(level, int):
            raise TypeError("Level must be str.")
        if level not in [DEBUG, INFO, WARNING, ERROR]:
            raise ValueError("Level must be in [DEBUG, INFO, WARNING, ERROR]")
        if not isinstance(log_format, str):
            raise TypeError("log_format must be str.")
        self.name = name
        self.level = level
        self.format = log_format
        self.logger = self.create_logger()


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


    def get_logger(self):
        """
        Get the logger object.

        :return: <Logger> - the logger
        """
        return self.logger


    def create_logger(self):
        """ Create the logger object using the init config. """
        return basicConfig(name=self.get_name(),
                           level=self.get_level(),
                           format=self.get_format())
