import logging

def main() -> None:
    logging.basicConfig(
        level= logging.DEBUG,
        format="%(asctime)s %(levelname)s >> %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename='simpleLog.log'
    )

    logging.info("Started my first logging file and program")

if __name__ == '__main__':
    main()