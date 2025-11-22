from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix.exceptions import VideoUnavailable
from pytubefix.cli import on_progress
from moviepy import VideoFileClip
import os
import asyncio
import concurrent.futures

luuVideo = r'C:/Users/hibis/Downloads/nhac'

def mp4_to_mp3(duongdan_video, duongdan_audio):
    video = VideoFileClip(duongdan_video)
    file_name = os.path.basename(duongdan_video)
    title = os.path.splitext(file_name)[0]
    duongdan_audio = os.path.join(duongdan_audio, title + ".mp3")
    video.audio.write_audiofile(duongdan_audio, codec='libmp3lame', bitrate='320k', fps=44100, logger=None)
    video.close()

    
async def taiVideos(duongdan, executor) -> None:
    def async_tai():
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
    await asyncio.get_event_loop().run_in_executor(executor, async_tai)

async def taiList(trang, max_concurrent=4) -> None:
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_concurrent) as executor:
        task = [
            taiVideos(video_url, executor)
            for video_url in Playlist(trang).video_urls
        ]
        await asyncio.gather(*task)
                

def layLink():
    while True:
        trang = input('Link video: ').strip()
        if trang == '': break
        elif trang == 'l':
            url_list = input('Link list video: ').strip()
            asyncio.run(taiList(trang=url_list))
        else:
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                asyncio.run(taiVideos(duongdan=trang, executor=executor))


if __name__ == "__main__":
    layLink()
