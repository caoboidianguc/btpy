from pytube import YouTube
from pytube import Playlist

#kiem tra version truoc khi chay chTrinh

while True :
    
    trang = input('Download 1 video: ')
    if trang == '': break

    try:
        yt = YouTube(trang)
        #yt.streams.filter(only_audio=True).first().download('D:\TaiVe')
        yt.streams.filter(resolution='720p').first().download()
        print('--Xong--')
    
    except :
        print(f'link nay:{trang} khong the download')






'''


#tai danh sach
dSach = input("Playlist: ")

try:
    danhsach = Playlist(dSach)
    print(f"Danh sach nay co {danhsach.length} video")
except:
    print("Khong tim thay danh sach nao")

else:
    for clip in danhsach.videos:
        clip.streams.filter(res="720").first().download('D:\TaiVe')
    print('--Xong--')

'''

