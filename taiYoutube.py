from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix.exceptions import VideoUnavailable
from pytubefix.cli import on_progress, display_progress_bar
from moviepy import VideoFileClip
import os

luuVideo = 'C:\\Users\\hibis\\Downloads\\nhac'
def mp4_to_mp3(duongdan_video, duongdan_audio):
    video = VideoFileClip(duongdan_video)
    file_name = os.path.basename(duongdan_video)
    title = os.path.splitext(file_name)[0]
    duongdan_audio = os.path.join(duongdan_audio, title + ".mp3")
    video.audio.write_audiofile(duongdan_audio, codec='libmp3lame', bitrate='320k', fps=44100, logger=None)
    video.close()
    
def taiVideos(duongdan):
    try:
        yt = YouTube(duongdan, on_progress_callback=on_progress)
    except VideoUnavailable as e:
        print(e)
        print('Video khong the down')
    else:
        yt = yt.streams.get_highest_resolution()
        print(f"Download...{yt.title} ")
        video = yt.download(luuVideo)
        mp4_to_mp3(video, luuVideo)
        os.remove(video)
        print(f"--{yt.title} --> Xong!")

def taiList():
    duongLink = input("Link List : ").strip()
    if not duongLink:
        print("Khong co link")
        return
    if duongLink == "":
        return
    ds = Playlist(duongLink)
    for url in ds.video_urls:
        taiVideos(url)
                


def layLink():
    while True:
        trang = input('Link video: ').strip()
        if trang == '': break
        elif trang == 'l':
            taiList()
        else:
            taiVideos(duongdan=trang)


if __name__ == "__main__":
    layLink()
