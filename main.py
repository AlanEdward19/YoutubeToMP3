import argparse
import logging
from datetime import date

from shared.middleware import check_if_file_exists


def main():
    parser = argparse.ArgumentParser(description='compara planilhas')
    parser.add_argument('--debug', action='store_true', help='Habilitar o debug')
    args = parser.parse_args()

    log_level = 20  # INFO LEVEL

    if args.debug:
        log_level = 10
    logging.basicConfig(filename=f'logs\youtube_to_mp3_{date.today()}.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | '
                               '%(message)s',
                        datefmt='%d/%m/%Y | %H:%M:%S', level=log_level)

    logging.info('Programa iniciado.')
    check_if_file_exists()


if __name__ == '__main__':
    main()
