from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QListView, \
    QLineEdit, QLabel, QTextEdit
from pytube import YouTube
from pytube import Playlist
from pytube import Channel


class F1(QWidget):
    def __init__(self):
        super().__init__()
        self.video_url = "https://youtu.be/rAr7uhKi2_k"
        self.channel_url = "https://www.youtube.com/channel/UC_grjqug_eF6bRS_fVezK-A/playlists"
        self.channel_name = "Hafnium"
        self.out_path = "/home/jll/kDrive2/Videos/Formations/"
        self.setup_ui()

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

    def print_playlists_channel(self, channel_url):
        url_list = self.get_playlists_channel(channel_url)
        for url in url_list:
            print(url)
        print("OK")

    def download_channel(self, channel_url, channel_name="", out_path=""):
        url_list = self.get_playlists_channel(channel_url)
        if bool(url_list):
            for url in url_list:
                path = f"{out_path}{channel_name}/"
                self.download_playlist(url, path)

    def download_playlist(self, playlist_url, out_path):
        p = Playlist(playlist_url)
        if bool(p):
            print(p.title)
            i = 0
            for url in p.video_urls:
                i = i + 1
                self.download_video(url, f"{out_path}{p.title}/", i)
            print("Fin de liste.")

    def download_video(self, video_url, out_path, order):
        video = YouTube(video_url)
        if bool(video):
            print(f"'{video.title}' dans '{out_path}'")

            video.register_on_progress_callback(self.on_progress_callback)
            # video.register_on_complete_callback(on_download_complete)
            video.streams.get_highest_resolution().download(output_path=f"{out_path}", filename_prefix=f"{str(order)}-")

    def on_progress_callback(self, stream, chunk, bytes_remaining):
        percent = (stream.filesize - bytes_remaining) * 100 / stream.filesize
        print(f"Download {int(percent)}%", end='\r')

    def on_download_complete(self, stream, file_path):
        print("OK")

    def on_click_btn_dowwnload(self):
        self.download_video(self.video_url, self.out_path, 1)

    def on_click_btn_quit(self):
        self.close()

    def setup_ui(self):
        self.setWindowTitle("Youtube")
        self.main_layout = QVBoxLayout(self)

        self.icons_layout = QHBoxLayout()
        for i in range(5):
            btn = QPushButton(f"{str(i)}")
            self.icons_layout.addWidget(btn)

        self.top_layout = QHBoxLayout()
        self.txt_url = QLineEdit()
        self.txt_output = QLineEdit()
        self.btn_output = QPushButton("...")
        self.top_layout.addWidget(self.txt_url)
        self.top_layout.addWidget(self.txt_output)
        self.top_layout.addWidget(self.btn_output)

        self.middle_layout = QHBoxLayout()
        self.list_playlist = QListView()
        self.middle_layout.addWidget(self.list_playlist)

        self.bottom_layout = QHBoxLayout()
        self.lab_log = QTextEdit()
        self.btn_quit = QPushButton("Quitter")
        self.btn_download = QPushButton("Download")
        self.btn_download.clicked.connect(self.on_click_btn_dowwnload)
        self.bottom_layout.addWidget(self.lab_log)
        self.btn_layout = QVBoxLayout()
        self.btn_layout.addWidget(self.btn_download)
        self.btn_layout.addWidget(self.btn_quit)
        self.bottom_layout.addLayout(self.btn_layout)

        self.main_layout.addLayout(self.icons_layout)
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addLayout(self.middle_layout)
        self.main_layout.addLayout(self.bottom_layout)
        # add connections
        self.btn_download.clicked.connect(self.on_click_btn_dowwnload)
        self.btn_quit.clicked.connect(self.on_click_btn_quit)

# app = QApplication()
# f1 = F1()
# f1.show()
# app.exec()
