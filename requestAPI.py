import json
import requests
def get_movies_from_tastedive(nhap):
    baseurl = "https://tastedive.com/api/similar"
    capdoi = {}
    capdoi['q'] = nhap
    capdoi['type'] = 'movies'
    capdoi['limit'] = 5
    #capdoi['callback'] = 'JSONP'
    thongtin = requests.get(baseurl, params=capdoi)
    print(thongtin.url)
    return thongtin.json()

phim = get_movies_from_tastedive("Black Panther")
print(phim)

def extract_movie_titles(phim):
    movielist = list()
    for name in phim['Similar']['Results']:
        movielist.append(name['Name'])
    return movielist

# movie = extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))

def get_related_titles(list):
    chuoiphi = []
    for item in list:
        mov = extract_movie_titles(get_movies_from_tastedive(item))
        for ph in mov:
            if ph not in chuoiphi:
                chuoiphi.append(ph)
    return chuoiphi

#phimlienquan = get_related_titles(["Black Panther", "Captain Marvel"])

def get_movie_data(tphim):#lay thong tin cua Phim
    burl = 'http://www.omdbapi.com/'
    thog = {}
    thog['t'] = tphim
    thog['r'] = 'json'
    gui = requests.get(burl,params=thog)
    print(gui.url)
    return gui.json()

#thongtin = get_movie_data("Venom")
def get_movie_rating(tenphim):
    di = 0
    for sou in tenphim['Ratings']:
        if sou['Source'] == 'Rotten Tomatoes':
            va = sou['Value']
            di = int(va[:2])
    return di


#diemphim = get_movie_rating(get_movie_data("Venom"))

def get_sorted_recommendations(list):
    
    tuiPhim = get_related_titles(list)
    diemTuiPhim = {}
    for movie in tuiPhim:
        diemTuiPhim[movie] = get_movie_rating(get_movie_data(movie))
        
    print(diemTuiPhim)
    return sorted(tuiPhim, key=lambda x: (-diemTuiPhim[x], diemTuiPhim)) #dau "-" truoc diemTuiPhim la xep phim tu cao xuong thap




#xapphim = get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])