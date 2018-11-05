# Author:taonyzhang
# Email:taonyzhang@gmail.com
# -*-coding:utf-8-*-

"""
从bing网站上，定时下载壁纸图片
"""
import urllib
import urllib.request
import json
import random
import time

WEB_ROOT = "https://cn.bing.com/"
path = "C:/Users/Administrator/Pictures/"

class BingSpider:

    def __init__(self, strPath):
        self.path = strPath

    def getHtml(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = urllib.request.Request(url=url, headers=headers)
        html = urllib.request.urlopen(req).read()
        print(html)
        js = json.loads(html)
        img_url = WEB_ROOT + js["images"][0]["url"]
        print(img_url)
        self.saveImg(img_url)

    def saveImg(self, imgUrl):
        strSavePath = self.path + time.strftime('%Y.%m.%d',time.localtime(time.time()))+"_"+str(random.randint(1, 999)) + ".jpg"
        urllib.request.urlretrieve(imgUrl, strSavePath)

    def run(self):
        for i in range(7):
            _url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=" + str(i) + "&n=1"
            self.getHtml(_url)

if __name__ == "__main__":
    spider = BingSpider(path)
    spider.run()
