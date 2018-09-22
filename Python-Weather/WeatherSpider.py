#-*-coding:UTF-8-*-

import urllib
import requests


URL="http://www.tianqihoubao.com/lishi/hangzhou/month/201801.html"

class WeatherSpider:

    def getHtml(self):
        r=requests.get(URL)
        print(r.text)


WeatherSpider spider= WeatherSpider()
spider.getHtml();

