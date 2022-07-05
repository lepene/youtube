# from youtube_gui import F1
# from PySide6.QtWidgets import QApplication
from pytube import YouTube
from pytube import Playlist
from pytube import Channel


def on_download_complete(stream, file_path):
    print("\tOK")


def on_progress_callback(stream, chunk, bytes_remaining):
    percent = int((stream.filesize - bytes_remaining) * 100 / stream.filesize)
    print(f"\rDownload {percent}%", end="")


def download_video(video_url, out_path, order):
    video = YouTube(video_url)
    video.register_on_progress_callback(on_progress_callback)
    video.register_on_complete_callback(on_download_complete)
    if bool(video):
        print(f"{out_path}{video.title}.mp4")
        video.streams.get_highest_resolution().download(output_path=f"{out_path}", filename_prefix=f"{str(order)}-")


def download_channel(channel_url, channel_name="", out_path=""):
    url_list = get_playlists_channel(channel_url)
    if bool(url_list):
        for url in url_list:
            path = f"{out_path}{channel_name}/"
            download_playlist(url, path)


def download_playlist(playlist_url, out_path):
    p = Playlist(playlist_url)
    if bool(p):
        print(p.title)
        i = 0
        for url in p.video_urls:
            i += 1
            download_video(url, f"{out_path}{p.title}/", i)
        print("Fin de liste.")


def print_playlist(playlist):
    p = Playlist(playlist)
    if bool(p):
        print(p.title)
        for url in p.video_urls:
            print(url)
        print("OK")


def get_playlists_channel(channel_url):
    url_list = []
    start = "playlist?list="
    end = '"'
    start_pos = 1
    end_pos = 1
    start_pos_previous = 0
    c = Channel(channel_url)
    html = c.playlists_html
    while start_pos >= start_pos_previous:
        start_pos = html.find(start, start_pos) + len(start)
        if start_pos >= start_pos_previous:
            end_pos = html.find(end, start_pos)
            url = f"https://www.youtube.com/playlist?list={html[start_pos:end_pos]}"
            url_list.append(url)
            start_pos_previous = start_pos
    return url_list


def print_playlists_channel(channel_url):
    url_list = get_playlists_channel(channel_url)
    for url in url_list:
        print(url)
    print("OK")


if __name__ == '__main__':
    # app = QApplication()
    # win1 = F1()
    # win1.show()
    # app.exec()
    video_url = "https://www.youtube.com/watch?v=D4xBM6zMjvs&list=PLFGnbArMpHtrGF2Q-zpEo7ojlI5h4CHvA"
    out_path = "/home/jll/Downloads/"
    if out_path != "" and video_url != "":
        if video_url.find("&list=") > 0:
            download_playlist(video_url, out_path)
        else:
            download_video(video_url, out_path, 1)
