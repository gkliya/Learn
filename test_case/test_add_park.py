# -*- coding:utf-8 -*-
# @Time     :2020/10/3 9:05
# @Author     :liyuan
# @File      :test_add_park.py
# @Software  :PyCharm
import requests
from config.conf import server_ip
from common.get_excel import *


def login():
    global token1
    username, password = get_excel_row(1)
    login_url = server_ip() + '/api/security/login'  # 登录接口
    data = {
        'username': username,
        'password': password
    }
    res = requests.post(login_url, data)
    token1 = res.headers['token']
    return token1
    # print(res.text)


def test_add_park():
    url = server_ip()+'/api/elephant/park/add'
    data = {'name': '测试',
        'parkType': '1',
        'foundTime': '2020/10/03',
        'longitude': '11',
        'latitude': '11',
        'phone': '13532653423',
        'placeProvince': '320000',
        'placeCity': '320100',
        'placeArea': '320116',
        'address': '11',
        'positioning': '大苏打',
        'industry':' 11'
          }
    headers={'Authorization': 'Bearer'+' ' + login()}
    res = requests.post(url=url,data=data,headers=headers)
    # print(res.json()['data']['id'])
    assert res.json()['msg'] == '请求成功'
    # return str(res.json()['data']['id'])


def test_delete_park():
    """先新增园区"""
    url = server_ip() + '/api/elephant/park/add'
    data = {'name': '测试1',
            'parkType': '1',
            'foundTime': '2020/10/03',
            'longitude': '11',
            'latitude': '11',
            'phone': '13532653423',
            'placeProvince': '320000',
            'placeCity': '320100',
            'placeArea': '320116',
            'address': '11',
            'positioning': '大苏打',
            'industry': ' 11'
            }
    headers = {'Authorization': 'Bearer' + ' ' + login()}
    res = requests.post(url=url, data=data, headers=headers)
    id = res.json()['data']['id']
    url1 = server_ip()+ '/api/elephant/park/delete?id={0}' .format(id)
    res1=requests.delete(url=url1,headers=headers)
    assert res1.json()['msg'] == '请求成功'


# test_add_park()
# test_delete_park()
