import re
import urllib.request


# -- 获取页面内容
def getHtml(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    html=urllib.request.urlopen(req).read()
    return html

# -- 获取页面图片
def getImg(html):
    reg = r'src="([.*\S]*\.jpg)"'
    imgre = re.compile(reg);
    imglist = re.findall(imgre, html)
    return imglist

# ------ getHtml()内输入任意帖子的URL ------

def dlImg(imgs):
    imgName = 0;
    for imgUrl in imgs:
        # ------ 这里最好使用异常处理及多线程编程方式 ------
        try:
            print(imgUrl);
            urllib.request.urlretrieve(imgUrl, 'C:\\Temp\\' + str(imgName) + '.jpg');
            imgName += 1;
        except Exception as e:
            print(e);
            print(imgUrl + " error")
        imgName += 1


def spide(url):
    html = getHtml(url)
    html = html.decode('UTF-8')
    imgs = getImg(html);
    if(len(imgs)>0):
        print("有数据");
        print(imgs);
        dlImg(imgs);
    else:
        print("未获取数据");


spide("http://huaban.com/");








