# -*-coding:utf-8-*-

import request
import urllib
from bs4 import BeautifulSoup
import re
import request
import json
import random


def getHtml(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    html = urllib.request.urlopen(req).read()
    print(html)

    soup = BeautifulSoup(html, "html.parser")
    imgs = soup.find_all("img")

    for img in imgs:
        print(img)
        # imgUrl = img.get("data-progressive")
        # saveImg(imgUrl)


def saveImg(imgUrl):
    print(imgUrl)
    path = "d:/" + str(random.randint(1, 99999)) + ".jpg"
    urllib.request.urlretrieve(imgUrl, path)


#getHtml("https://bing.ioliu.cn")
getHtml("https://cn.bing.com/HPImageArchive.aspx?format=js&idx=1&n=1")