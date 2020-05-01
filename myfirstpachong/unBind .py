# -*- coding: utf-8 -*-
# @Time : 2020/4/19 19:34
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : lianxi01
# @Project : pachong
import requests
import urllib.parse
import urllib.request

url ="http://user.ws.126.net/api/v2/commons/login/ext/unBind"
d = bytes(urllib.parse.urlencode({"token":"unBind","passport":"ogm9zs38ww473f7b90e3361b1c465341ecca69b445@wx.163.com"}), encoding='utf8')
headers ={ "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36","Content-Type": "application/x-www-form-urlencoded"}
r = requests.post(url,headers=headers,data=d)
print(r.url)
print(r.status_code)



