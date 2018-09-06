# -*-coding:utf-8-*-

import request
import urllib
from bs4 import BeautifulSoup
import re
import request
import json
import random

img_root="https://cn.bing.com/"

def getHtml(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    html = urllib.request.urlopen(req).read()
    print(html)
    js=json.loads(html)
    img_url=js["images"][0]["url"]
    print(img_url)
    saveImg(img_root+img_url)

def saveImg(imgUrl):
    print(imgUrl)
    path = "d:/" + str(random.randint(1, 99999)) + ".jpg"
    urllib.request.urlretrieve(imgUrl, path)

getHtml("https://cn.bing.com/HPImageArchive.aspx?format=js&idx=1&n=1")