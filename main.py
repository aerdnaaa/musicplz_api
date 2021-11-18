from fastapi import FastAPI
from pytube import YouTube
from moviepy.editor import *

app = FastAPI()

@app.get("/video/")
def download_music(url: str = '', music_only: bool = True):
    youtube_obj = YouTube(url).streams.filter(only_audio=True).all()
    youtube_obj[0].download(output_path='./downloads')
    return url