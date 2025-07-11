import logging 
from logging.handlers import SysLogHandler

HOST= 'xyja;j;jz.com'
PORT= 15444

def main() -> None:
    logger = logging.getLogger('TalibanCodes')
    logger.setLevel(logging.DEBUG)
    handler = SysLogHandler(address=(HOST, PORT))
    logger.addHandler(handler)

    logger.debug("I want to debug my code")

if __name__ == '__main__':
    main()