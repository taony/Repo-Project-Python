# -*-coding:utf-8-*-
"""
从bing网站上，定时下载壁纸图片
"""
import request
import urllib
from bs4 import BeautifulSoup
import re
import request
import json
import random

img_root = "https://cn.bing.com/"


class BingSpider:

    def getHtml(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = urllib.request.Request(url=url, headers=headers)
        html = urllib.request.urlopen(req).read()
        print(html)
        js = json.loads(html)
        img_url = js["images"][0]["url"]
        print(img_url)
        self.saveImg(img_root + img_url)

    def saveImg(imgUrl):
        path = "C:/Users/Administrator/Pictures/" + str(random.randint(1, 99999)) + ".jpg"
        urllib.request.urlretrieve(imgUrl, path)

    def run(self):
        for i in range(7):
            self.getHtml("https://cn.bing.com/HPImageArchive.aspx?format=js&idx=" + str(i) + "&n=1")

spider=BingSpider()
spider.run();