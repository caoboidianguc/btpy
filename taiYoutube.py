
from pytube import YouTube
from pytube import Playlist
import pytube.exceptions

#Successfully uninstalled pytube-10.9.3
#kiem tra version truoc khi chay chTrinh

while True :
    
    trang = input('Download 1 video: ')
    if trang == '': break

    try:
        yt = YouTube(trang)
        #can xem lai filter neu muon video
        yt.streams.filter(only_audio=True).first().download('C:\\Users\\hibis\\Downloads\\taiTube')

        #yt.streams.filter(only_audio=True).first().download('C:\\Users\\hibis\\Downloads\\taiTube')
        #yt.streams.filter(resolution='720p').first().download('C:\\Users\\hibis\\Downloads\\taiTube')
        print("--Xong--") 
    
    except pytube.exceptions.ExtractError as e:
        print(e)
        print(f'link nay:-- {trang} -- khong dung dia chi')
  





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

