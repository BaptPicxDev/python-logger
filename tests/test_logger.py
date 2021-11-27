"""
    Created by: Baptiste PICARD
    Date: 27/11/2021
    Contact: picard.baptiste22@gmail.com

    Test the logger.
"""

# Imports.
import sys
from os import remove
from os.path import (
    join,
    abspath,
    exists
)
import pytest

# Environment
sys.path.append(join(abspath('.'), 'source'))

# Project modules.
from logger import (
    HomemadeLogger,
    basicConfig,
    HomemadeTimedRotatingFileHandler,
    TimedRotatingFileHandler,
    INFO,
    DEBUG,
    ERROR,
)


class TestHomemadeLogger:
    """
        Test the class HomemadeLogger.
    """

    def setup_class(self):
        """ Setup function called before each test. """
        pass

    def teardown_class(self):
        """ Setup function called before each test. """
        if exists('log'):
            remove('log')
        if exists('test_log'):
            remove('test_log')

    def test_get_name(self):
        """ Test the HomemadeLogger.get_name function. """
        with pytest.raises(TypeError):
            HomemadeLogger(name=1)
            HomemadeLogger(name=True)
            HomemadeLogger(name=[])
            HomemadeLogger(name={})
        logger_name = 'My new logger'
        logger = HomemadeLogger()
        assert logger.get_name() == 'My Own Logger'
        logger = HomemadeLogger(name=logger_name)
        assert logger.get_name() == logger_name

    def test_get_level(self):
        """ Test the HomemadeLogger.get_level function. """
        with pytest.raises(TypeError):
            HomemadeLogger(level='')
            HomemadeLogger(name=True)
            HomemadeLogger(name=[])
            HomemadeLogger(name={})
        with pytest.raises(ValueError):
            HomemadeLogger(level=1)
            HomemadeLogger(level=11)
            HomemadeLogger(level=42)
        logger_level = ERROR
        logger = HomemadeLogger()
        assert logger.get_level() == INFO
        logger = HomemadeLogger(level=logger_level)
        assert logger.get_level() == ERROR

    def test_get_format(self):
        """ Test the HomemadeLogger.get_format function. """
        with pytest.raises(TypeError):
            HomemadeLogger(log_format=1)
            HomemadeLogger(name=True)
            HomemadeLogger(name=[])
            HomemadeLogger(name={})
        logger_format = "my new format"
        logger = HomemadeLogger()
        assert logger.get_format() == "%(asctime)s %(message)s"
        logger = HomemadeLogger(log_format=logger_format)
        assert logger.get_format() == logger_format

    def test_get_logger(self):
        """ Test the HomemadeLogger.get_logger function. """
        with pytest.raises(TypeError):
            HomemadeLogger(name=1,
                           level=INFO,
                           log_format='format')
            HomemadeLogger(name='Test logger',
                           level=[INFO, DEBUG],
                           log_format='format')
            HomemadeLogger(name='Test logger',
                           level=DEBUG,
                           log_format={'format': 1})
        with pytest.raises(ValueError):
            HomemadeLogger(name='This is a test',
                           level=42,
                           log_format='test')
        homemade_logger = HomemadeLogger(name='This is a test',
                                         level=DEBUG,
                                         log_format='test')
        assert isinstance(homemade_logger.get_logger(), type(basicConfig()))


class TestHomemadeTimedRotatingFileHandler:
    """
        Test the class HomemadeTimedRotatingFileHandler.
    """

    def setup_class(self):
        """ Setup function called before each test. """
        pass

    def teardown_class(self):
        """ Setup function called before each test. """
        if exists('log'):
            remove('log')
        if exists('test_log'):
            remove('test_log')

    def test_get_name(self):
        """ Test the HomemadeTimedRotatingFileHandler.get_name function. """
        with pytest.raises(TypeError):
            HomemadeTimedRotatingFileHandler(filename=1)
            HomemadeTimedRotatingFileHandler(filename=True)
            HomemadeTimedRotatingFileHandler(filename=[])
            HomemadeTimedRotatingFileHandler(filename={})
        test_filename = 'test_log'
        handler = HomemadeTimedRotatingFileHandler()
        assert handler.get_filename() == 'log'
        handler = HomemadeTimedRotatingFileHandler(filename=test_filename)
        assert handler.get_filename() == test_filename

    def test_get_when(self):
        """ Test the HomemadeTimedRotatingFileHandler.get_when function. """
        with pytest.raises(TypeError):
            HomemadeTimedRotatingFileHandler(when=1)
            HomemadeTimedRotatingFileHandler(when=True)
            HomemadeTimedRotatingFileHandler(when=[])
            HomemadeTimedRotatingFileHandler(when={})
        with pytest.raises(ValueError):
            HomemadeTimedRotatingFileHandler(when='hello')
            HomemadeTimedRotatingFileHandler(when='SS')
        test_when = 'w2'
        handler = HomemadeTimedRotatingFileHandler()
        assert handler.get_when() == 'H'
        handler = HomemadeTimedRotatingFileHandler(when=test_when)
        assert handler.get_when() == test_when.upper()

    def test_get_interval(self):
        """ Test the HomemadeTimedRotatingFileHandler.get_interval function. """
        with pytest.raises(TypeError):
            HomemadeTimedRotatingFileHandler(interval='')
            HomemadeTimedRotatingFileHandler(when=True)
            HomemadeTimedRotatingFileHandler(when=[])
            HomemadeTimedRotatingFileHandler(when={})
        test_interval = 1
        handler = HomemadeTimedRotatingFileHandler()
        assert handler.get_interval() == 1
        handler = HomemadeTimedRotatingFileHandler(interval=test_interval)
        assert handler.get_interval() == test_interval

    def test_get_handler(self):
        """ Test the HomemadeTimedRotatingFileHandler.get_handler function. """
        with pytest.raises(TypeError):
            HomemadeTimedRotatingFileHandler(filename=1,
                                             when='S or H',
                                             interval=1,
                                             log_format='format')
            HomemadeTimedRotatingFileHandler(filename='test filename',
                                             when=['S', 'H'],
                                             interval=1,
                                             log_format='format')
            HomemadeTimedRotatingFileHandler(filename='test filename',
                                             when='w6',
                                             interval='1',
                                             log_format='format')
            HomemadeTimedRotatingFileHandler(filename='test filename',
                                             when='w6',
                                             interval=1,
                                             log_format=['This format should works'])
        with pytest.raises(ValueError):
            HomemadeTimedRotatingFileHandler(filename='test filename',
                                             when='Minute',
                                             interval=1,
                                             log_format='format')
        handler = HomemadeTimedRotatingFileHandler()
        assert isinstance(handler.get_handler(),
                          type(TimedRotatingFileHandler(filename='log')))
