# FileHandler 클래스를 이용하여 로그 파일 분할하여 저장하기

import logging

logging.basicConfig(level=logging.DEBUG)

debug_logger = logging.getLogger('debug_log')
debug_logger.setLevel(logging.DEBUG)

logFileHandler = logging.FileHandler('debug.log')
logFileHandler.setLevel(logging.DEBUG)

debug_logger.addHandler(logFileHandler)

logging.debug("DEBUG log message - Console")
debug_logger.debug("DEBUG log message - File")