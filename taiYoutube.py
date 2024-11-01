
from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix.exceptions import VideoUnavailable
from pytubefix.cli import on_progress, display_progress_bar

# pip install pytubefix

def taiVideos(duongdan):
    try:
        yt = YouTube(duongdan, on_progress_callback = on_progress, on_complete_callback= display_progress_bar)
    except VideoUnavailable as e:
        print(e)
        print('Video khong the down')
    else:
        # yt.streams.get_audio_only()
        yt = yt.streams.get_highest_resolution()
        print(f"Download...{yt.title} ")
        yt.download('C:\\Users\\hibis\\Downloads\\nhac')
        # yt.download(mp3=True)
        print(f"--{yt.title} --> Xong!")
    
    


def taiList():
    duongdan = input("Link List : ")
    if duongdan == "":
        return
    ds = Playlist(duongdan)
    for video in ds.videos:
        taiVideos(video)
                


def layLink():
    while True:
        trang = input('Link video: ')
        if trang == '': break
        elif trang == 'l':
            taiList()
        else:
            taiVideos(duongdan=trang)


if __name__ == "__main__":
    layLink()