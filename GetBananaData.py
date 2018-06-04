from urllib import request
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time

url= 'https://search.daum.net/search?nil_suggest=btn&nil_ch=&rtupcoll=&w=img&m=&f=&lpp=&DA=SBC&sug=&sq=&o=&sugo=&q=%EA%B3%BC%EC%9D%BC+%EB%B0%B0'
browser =  webdriver.Chrome(executable_path='./chromedriver.exe')
browser.implicitly_wait(3)
browser.get(url)
lastLength = browser.execute_script('return document.body.scrollHeight;')
for i in range(30):
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(0.5)

getHtml = bs(browser.page_source, 'html.parser')
bananaSrc = getHtml.findAll('img')
bananaSrc = bananaSrc[2:]


for i, banana in enumerate(bananaSrc):
    try:
        i = i+500
        print(banana.get('src'))
        request.urlretrieve(banana.get('src'), './peach/'+str(i)+'.jpg')
    except:
        pass
