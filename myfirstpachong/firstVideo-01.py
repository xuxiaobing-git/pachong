# -*- coding: utf-8 -*-
# @Time : 2020/4/17 20:20
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : firstVideo-01.py
# @Project : pachong
import requests
from bs4 import BeautifulSoup

url = "https://www.bilibili.com/ranking"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400"}
cookie = {"cookie":"bsource=seo_baidu; _uuid=CC2079C2-1C2F-781B-2287-345CB08E0C8A28560infoc; buvid3=9570BBBC-59FF-4B5A-869F-077B14E6983953942infoc; CURRENT_FNVAL=16; sid=94n5u4lv; LIVE_BUVID=AUTO6415869539278481; PVID=1"}
Params={"spm_id_from":"333.5.b_7072696d61727950616765546162.3"}
r=requests.get(url=url,params=Params,headers=headers,cookies=cookie)
html=r.text
soup = BeautifulSoup(html, 'html.parser')
items = soup.find(attrs={"class":"rank-list"}).children
for item in items:
    if item == '\n': continue
    title = item.find(attrs={'class': 'title'}).string.strip()
    videolink=item.find(attrs={'class': 'info'}).a["href"]
    #videolist=title+videolink
    with open('shipinliebiao.txt', "a+", encoding="utf-8") as f:
        f.write("【#推荐视频#"+title +"】"+videolink+'\n'+'\n')
        #print("视频标题："+title    ,  "视频URL："+videolink)

        3669


