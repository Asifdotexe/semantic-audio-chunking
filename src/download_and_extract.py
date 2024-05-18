import pytube
import moviepy as mp

def download(url, output_path=None):
    yt = pytube.YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    video.download(output_path)