from pathlib import Path
from shared.utils.dowloadYoutube import youtube_converter
from shared.utils.downloadYoutubeMultipleLinks import youtube_converter_multiple_links

import asyncio

import logging

def check_if_file_exists():
    logging.info('Verificando se existe arquivo de texto com varios links')
    file = Path("musicas.txt")

    if file.exists():
        logging.info("Arquivo encontrado")
        asyncio.run(youtube_converter_multiple_links()) 
    
    else:
        url = input("digite a url do video:")
        logging.info("Arquivo não encontrado, iniciando dowload por link unico")
        youtube_converter(url)
