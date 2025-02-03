from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

# https://pypi.org/project/pytubefix/ 

url = input("URL do vídeo do YouTube: ")

path = os.path.join(os.getcwd(), "videos")

os.makedirs(path, exist_ok=True)

yt = YouTube(url, on_progress_callback=on_progress)

print(f"Baixando: {yt.title}")

ys = yt.streams.get_highest_resolution()

ys.download(output_path=path)
print(f"Download completo! O vídeo foi salvo em: {path}")