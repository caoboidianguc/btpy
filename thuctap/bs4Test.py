from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error


url = 'https://www.thongluan.blog/?m=1'
layweb = urllib.request.urlopen(url)

soup = BeautifulSoup(layweb, 'lxml')
tag = soup.find_all('a')
print(tag)