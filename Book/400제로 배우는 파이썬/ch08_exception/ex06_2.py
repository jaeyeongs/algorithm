# 여러 종류의 로그 발생 예제

import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(asctime)s - %(message)s')

logging.info("INFO log message")
logging.warning("WARNING log message")
logging.debug("DEBUG log message")
logging.error("ERROR log message")
logging.critical("CRITICAL log message")