from os.path import (
    join,
    abspath
)
import sys
sys.path.append(join(abspath('.'), 'source'))
from logger import (
    HomemadeLogger,
    HomemadeTimedRotatingFileHandler
)
import time

if __name__ == '__main__':
    LOGGER_NAME = 'TEST'
    obj = HomemadeLogger(
        name=LOGGER_NAME,
        handlers=[
            HomemadeTimedRotatingFileHandler(interval=1)
        ]
    )
    logger = obj.get_logger()
    for i in range(5):
        obj.log('test')
        time.sleep(5)