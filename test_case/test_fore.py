# -*- coding:utf-8 -*-
# @Time     :2020/9/30 11:52
# @Author     :liyuan
# @File      :test_fore.py
# @Software  :PyCharm


import requests
from config.conf import server_ip
from common.get_excel import *

for i in range(1,get_excel_nrows()):
    username,password=get_excel_row(i)
    login_url = server_ip()+ '/api/security/login'#登录接口
    data = {
        'username': username,
        'password': password
    }
    res = requests.post(login_url, data)
    # print(res.headers['token'])
    print(res.text)


# talent_list_url = server_ip()+ '/api/elephant/talent/list/1/10?timestamp=1601430897070'
# headers = {'Authorization': 'Bearer 92b3968c-e7e5-4b46-8ff0-54a786989954'
#        }
# res1 = requests.get(url=talent_list_url, headers=headers)
# print(res1.text)

