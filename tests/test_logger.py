"""
    Created by: Baptiste PICARD
    Date: 27/11/2021
    Contact: picard.baptiste22@gmail.com

    Test the logger.
"""

# Imports.
from os import remove
from os.path import (
    join,
    abspath,
    exists
)
import pytest
from unittest import TestCase

# Environment
import sys
sys.path.append(join(abspath('.'), 'source'))

# Project modules.
from logging import Logger
from logger import (
    HomemadeLogger,
    HomemadeTimedRotatingFileHandler,
    TimedRotatingFileHandler,
    INFO,
    DEBUG,
    ERROR,
)


class TestHomemadeLogger(TestCase):
    """
        Test the class HomemadeLogger.
    """

    def setup_class(self):
        """ Setup function called before each test. """
        self.test_logger_name = 'My new logger'
        self.test_logger_name_1 = 'My new logger 1'
        self.test_logger_level = ERROR
        self.test_logger_level_1 = DEBUG
        self.test_logger_format = "%(asctime)s - %(name)s - %(levelname)s"
        self.test_logger_format_1 = "%(asctime)s - %(name)s"
        self.test_message = 'How'
        self.test_message_1 = 'Are'

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
        logger = HomemadeLogger()
        assert logger.get_name() == 'my_own_logger'
        logger = HomemadeLogger(name=self.test_logger_name)
        assert logger.get_name() == (self.test_logger_name
                                     .strip().lower()
                                     .replace(' ', '_'))
        logger = HomemadeLogger(name=self.test_logger_name_1)
        assert logger.get_name() == (self.test_logger_name_1
                                     .strip().lower()
                                     .replace(' ', '_'))

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
        logger = HomemadeLogger()
        assert logger.get_level() == INFO
        logger = HomemadeLogger(level=self.test_logger_level)
        assert logger.get_level() == self.test_logger_level
        logger = HomemadeLogger(level=self.test_logger_level_1)
        assert logger.get_level() == self.test_logger_level_1

    def test_get_format(self):
        """ Test the HomemadeLogger.get_format function. """
        with pytest.raises(TypeError):
            HomemadeLogger(log_format=1)
            HomemadeLogger(name=True)
            HomemadeLogger(name=[])
            HomemadeLogger(name={})
        logger = HomemadeLogger()
        assert logger.get_format() == "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        logger = HomemadeLogger(log_format=self.test_logger_format)
        assert logger.get_format() == self.test_logger_format
        logger = HomemadeLogger(log_format=self.test_logger_format_1)
        assert logger.get_format() == self.test_logger_format_1

    def test_get_logger(self):
        """ Test the HomemadeLogger.get_logger function. """
        homemade_logger = HomemadeLogger(name='This is a test',
                                         level=DEBUG,
                                         log_format='test').get_logger()
        assert homemade_logger.hasHandlers()
        assert isinstance(homemade_logger, Logger)

    def test_init(self):
        """ Test the HomemadeLogger.__init__ function. """
        with pytest.raises(TypeError):
            HomemadeLogger(name=1,
                           level=INFO,
                           log_format='format',
                           handllers=[])
            HomemadeLogger(name='Test logger',
                           level=[INFO, DEBUG],
                           log_format='format',
                           handllers=[])
            HomemadeLogger(name='Test logger',
                           level=DEBUG,
                           log_format={'format': 1},
                           handllers=[])
            HomemadeLogger(name='Test logger',
                           level=DEBUG,
                           log_format='format',
                           handllers={})
            HomemadeLogger(name='Test logger',
                           level=DEBUG,
                           log_format='format',
                           handllers=TimedRotatingFileHandler)
        with pytest.raises(ValueError):
            HomemadeLogger(name='This is a test',
                           level=42,
                           log_format='test')

    def test_logging(self):
        logger = HomemadeLogger().get_logger()
        with self.assertLogs() as captured:
            logger.log(INFO, self.test_message)
            logger.log(ERROR, self.test_message_1)
        assert len(captured.records) == 2
        assert captured.records[0].getMessage() == self.test_message
        assert captured.records[0].levelname == 'INFO'
        assert captured.records[1].getMessage() == self.test_message_1
        assert captured.records[1].levelname == 'ERROR'


class TestHomemadeTimedRotatingFileHandler:
    """
        Test the class HomemadeTimedRotatingFileHandler.
    """

    def setup_class(self):
        """ Setup function called before each test. """
        self.test_filename = 'test_log'
        self.test_filename_1 = 'test_log_1'
        self.test_when = 'w2'
        self.test_when_1 = 'Midnight'
        self.test_interval = 1
        self.test_interval_1 = 100

    def teardown_class(self):
        """ Setup function called before each test. """
        if exists('log'):
            remove('log')
        if exists(self.test_filename):
            remove(self.test_filename)
        if exists(self.test_filename_1):
            remove(self.test_filename_1)

    def test_get_name(self):
        """ Test the HomemadeTimedRotatingFileHandler.get_name function. """
        with pytest.raises(TypeError):
            HomemadeTimedRotatingFileHandler(filename=1)
            HomemadeTimedRotatingFileHandler(filename=True)
            HomemadeTimedRotatingFileHandler(filename=[])
            HomemadeTimedRotatingFileHandler(filename={})
        handler = HomemadeTimedRotatingFileHandler()
        assert handler.get_filename() == 'log'
        handler = HomemadeTimedRotatingFileHandler(filename=self.test_filename)
        assert handler.get_filename() == self.test_filename
        handler = HomemadeTimedRotatingFileHandler(filename=self.test_filename_1)
        assert handler.get_filename() == self.test_filename_1

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
        handler = HomemadeTimedRotatingFileHandler()
        assert handler.get_when() == 'H'
        handler = HomemadeTimedRotatingFileHandler(when=self.test_when)
        assert handler.get_when() == self.test_when.upper()
        handler = HomemadeTimedRotatingFileHandler(when=self.test_when_1)
        assert handler.get_when() == self.test_when_1.upper()

    def test_get_interval(self):
        """ Test the HomemadeTimedRotatingFileHandler.get_interval function. """
        with pytest.raises(TypeError):
            HomemadeTimedRotatingFileHandler(interval='')
            HomemadeTimedRotatingFileHandler(interval=True)
            HomemadeTimedRotatingFileHandler(interval=[])
            HomemadeTimedRotatingFileHandler(interval=[100])
            HomemadeTimedRotatingFileHandler(interval={})
        with pytest.raises(ValueError):
            HomemadeTimedRotatingFileHandler(interval=-1)
            HomemadeTimedRotatingFileHandler(interval=0)
        handler = HomemadeTimedRotatingFileHandler()
        assert handler.get_interval() == 1
        handler = HomemadeTimedRotatingFileHandler(interval=self.test_interval)
        assert handler.get_interval() == self.test_interval
        handler = HomemadeTimedRotatingFileHandler(interval=self.test_interval_1)
        assert handler.get_interval() == self.test_interval_1

    def test_get_handler(self):
        """ Test the HomemadeTimedRotatingFileHandler.get_handler function. """
        handler = HomemadeTimedRotatingFileHandler()
        assert isinstance(handler.get_handler(),
                          type(TimedRotatingFileHandler(filename='log')))

    def test_init(self):
        """ Test the HomemadeTimedRotatingFileHandler.__init__ function. """
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
            HomemadeTimedRotatingFileHandler(filename='test filename',
                                             when='Minute',
                                             interval=-42,
                                             log_format='format')
