# -*- coding: utf-8 -*-
# @Time : 2020/4/19 19:34
# @Author : Administrator
# @Email : xu19890913@163.com
# @File : lianxi01
# @Project : pachong
import requests

url ="http://user.ws.126.net/api/v2/commons/login/ext/unBind/"
d = {"header":"Content-Type: application/x-www-form-urlencoded","token":"unBind","passport":"6c43ec2fabd35dd74bd3a4ea67ad53b7@tencent.163.com"}
r = requests.post(url,data=d)
print(r.url)
print(r.status_code)

