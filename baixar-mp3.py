from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

url = input("URL do vídeo do YouTube: ")

path = os.path.join(os.getcwd(), "áudios")
os.makedirs(path, exist_ok=True)

yt = YouTube(url, on_progress_callback=on_progress)

print(f"Baixando o áudio do vídeo: {yt.title}")

ys = yt.streams.get_audio_only()

ys.download(output_path=path, filename=f"{yt.title}.mp3")

print(f"Download completo! O áudio foi salvo em: {path}")
