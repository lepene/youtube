from pytube import YouTube
from pytube import Playlist
from pytube import Channel


def print_playlists_channel(channel_url):
    url_list = get_playlists_channel(channel_url)
    for url in url_list:
        print(url)
    print("OK")


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


def download_channel(channel_url, channel_name):
    url_list = get_playlists_channel(channel_url)
    if bool(url_list):
        for url in url_list:
            print(url)
            download_playlist(url, f"/home/jll/Downloads/{channel_name}/")
    # start = "playlist?list="
    # end = '"'
    # start_pos = 1
    # end_pos = 1
    # start_pos_previous = 0
    # c = Channel(channel_url)
    # html = c.playlists_html
    # while start_pos >= start_pos_previous:
    #     start_pos = html.find(start, start_pos) + len(start)
    #     if start_pos >= start_pos_previous:
    #         end_pos = html.find(end, start_pos)
    #         url = f"https://www.youtube.com/playlist?list={html[start_pos:end_pos]}"
    #         print(url)
    #         download_playlist(url, f"/home/jll/Downloads/{channel_name}/")
    #         start_pos_previous = start_pos


def download_playlist(playlist_url, out_path):
    p = Playlist(playlist_url)
    if bool(p):
        print(p.title)
        i = 0
        for url in p.video_urls:
            i = i + 1
            download_video(url, f"{out_path}{p.title}/", i)
        print("Fin de liste.")


def download_video(video_url, out_path, order):
    video = YouTube(video_url)
    if bool(video):
        print(video.title)
        video.register_on_progress_callback(on_progress_callback)
        video.register_on_complete_callback(on_download_complete)
        video.streams.get_highest_resolution().download(output_path=f"{out_path}", filename_prefix=f"{str(order)}-")


def on_progress_callback(stream, chunk, bytes_remaining):
    percent = (stream.filesize - bytes_remaining) * 100 / stream.filesize
    print(f"Download {int(percent)}%")


def on_download_complete(stream, file_path):
    print("OK")


if __name__ == '__main__':
    channel_url = "https://www.youtube.com/c/Docstring/playlists"
    channel_name = "Docstrings"
    print_playlists_channel(channel_url)
#    download_channel(channel_url, channel_name)
