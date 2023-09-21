from shared.utils.dowloadYoutube import youtube_converter
from sys import platform
import asyncio

if platform == "win32":
   asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

async def youtube_converter_multiple_links():
    file = open("musicas.txt", "r")
    
    # reading the file
    data = file.read()

    musics = data.split("\n")

    await asyncio.gather(*[youtube_converter(music) for music in musics])
    
    file.close()