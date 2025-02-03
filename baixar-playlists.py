from pytubefix import Playlist
import os

url = input("URL da playlist do YouTube: ")

path = os.path.join(os.getcwd(), "playlists")
os.makedirs(path, exist_ok=True)

pl = Playlist(url)

print(f"Baixando áudios da playlist: {pl.title}")

for video in pl.videos:
    print(f"Baixando o áudio do vídeo: {video.title}")
    ys = video.streams.get_audio_only()
    ys.download(output_path=path, filename=f"{video.title}.mp3")

print("Download completo! Todos os áudios foram salvos em:", path)