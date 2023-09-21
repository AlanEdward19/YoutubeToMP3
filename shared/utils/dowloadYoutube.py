import youtube_dl
import logging as log

def youtube_converter(video_url: str):

    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,
        download=False
    )

    filename = f"/music/{video_info['title']}.mp3"
    log.info(f"Arquivo de nome: {video_info['title']} adquirido")
    
    options = {
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
        log.info(f"Arquivo de nome: {video_info['title']} baixado!!")