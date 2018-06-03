from urllib import request
import requests
from bs4 import BeautifulSoup as bs

session = requests.session()

html = session.get('https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EB%B0%94%EB%82%98%EB%82%98')
print(html.text)
getHtml = bs(html.text, 'html.parser')
bananaSrc = getHtml.findAll('img')
bananaImgTag = bananaSrc[1:]
print(bananaImgTag)
for i, banana in enumerate(bananaImgTag):
     request.urlretrieve(banana.get('src'), './bananaData/'+str(i)+'.jpg')

