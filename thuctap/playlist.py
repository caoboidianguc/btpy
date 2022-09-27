from pytube import Playlist, YouTube


dgdan = "https://www.youtube.com/watch?v=3tmd-ClpJxA&list=RDe-ORhEE9VVg&index=3"

danhsach = Playlist(dgdan)
for dg in danhsach.video_urls:
    print(dg)
'''
for linkdan in danhsach.title:
    
    try :
        linkdown = YouTube(linkdan)
        linkdown.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    except VideoUnavailable:
        print(f"duong dan {linkdan} khong truy cap duoc")
'''
