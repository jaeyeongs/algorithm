# 로그를 파일에 저장하기

import logging

logging.basicConfig(filename='logfile.txt',
                    level=logging.DEBUG,
                    format='%(levelname)s - %(asctime)s - %(message)s')

logging.debug("Some message")