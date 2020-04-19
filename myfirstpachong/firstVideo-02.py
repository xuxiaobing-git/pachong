# -*- coding: utf-8 -*-
# @Time : 2020/4/18 14:42
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : firstVideo-02.py
# @Project : pachong
import requests
from bs4 import BeautifulSoup
import time


class Find():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 \Core/1.70.3756.400 QQBrowser/10.5.4039.400"}
    cookie = {
        "cookie": "bsource=seo_baidu; _uuid=CC2079C2-1C2F-781B-2287-345CB08E0C8A28560infoc; \
                buvid3=9570BBBC-59FF-4B5A-869F-077B14E6983953942infoc; CURRENT_FNVAL=16; \
                sid=94n5u4lv; LIVE_BUVID=AUTO6415869539278481; PVID=1"}

    def __init__(self):
        self.url = "https://www.bilibili.com/ranking"
        self.url_1 = ""
        self.Params = {"spm_id_from": "333.5.b_7072696d61727950616765546162.3"}

    def tok(self):

        self.dict_name = {}
        r = requests.get(url=self.url, params=self.Params, headers=self.headers, cookies=self.cookie)
        html = r.text
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find(attrs={"class": "rank-list"}).children
        for item in items:
            if item == '\n': continue
            title = item.find(attrs={'class': 'title'}).string.strip()
            videolink = item.find(attrs={'class': 'info'}).a["href"]
            self.dict_name[title]=videolink
        return self.dict_name

    def write_it(self):
        tt=self.tok()
        dict_2=tt
        for i in tt:
            with open('shipinliebiao.txt', 'a+', encoding="utf-8") as f:
             f.write("【#推荐视频#" + i + "】" + dict_2[i] + '\n' + '\n')


if __name__ == '__main__':
    b = Find()
    ttt=b.tok()
    print("文件已经生成")
    b.write_it()


