import logging
import sys


def terminate(exit_code):
    logging.info('Encerrando o programa.')
    sys.exit(exit_code)
