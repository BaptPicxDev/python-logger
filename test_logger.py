"""
    Created by: Baptiste PICARD
    Date: 27/11/2021
    Contact: picard.baptiste22@gmail.com

    Test the logger.
"""

## Imports.
import pytest

## Project modules.
from logger import (
    Logger,
    INFO,
    ERROR,
)

## Functions.

## Classes.
class TestLogger:
    """
        Test the class Logger.
    """

    def test_get_name(self, logger_name='My new logger'):
        """ First test. """
        with pytest.raises(TypeError):
            Logger(name=1)
            Logger(name=True)
            Logger(name=[])
            Logger(name={})
        logger = Logger()
        assert logger.get_name() == 'My Own Logger'
        logger = Logger(name=logger_name)
        assert logger.get_name() == logger_name


    def test_get_level(self, logger_level=ERROR):
        """ First test. """
        with pytest.raises(TypeError):
            Logger(level='')
            Logger(name=True)
            Logger(name=[])
            Logger(name={})
        with pytest.raises(ValueError):
            Logger(level=1)
            Logger(level=11)
            Logger(level=42)
        logger = Logger()
        assert logger.get_level() == INFO
        logger = Logger(level=logger_level)
        assert logger.get_level() == ERROR


    def test_get_format(self, logger_format="my new format"):
        """ First test. """
        with pytest.raises(TypeError):
            Logger(log_format=1)
            Logger(name=True)
            Logger(name=[])
            Logger(name={})
        logger = Logger()
        assert logger.get_format() == "%(asctime)s %(message)s"
        logger = Logger(log_format=logger_format)
        assert logger.get_format() == logger_format
