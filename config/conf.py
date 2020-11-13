# -*- coding:utf-8 -*-
# @Time     :2020/9/30 11:45
# @Author     :liyuan
# @File      :conf.py
# @Software  :PyCharm


def server_ip():
    """
    返回需要测试的环境IP
    :return:
    """
    test_ip = 'http://192.168.20.116:998'
    production_environment = 'http://113.105.131.146'
    return production_environment


def sql_cof():
    host, user, password,database, port, charset = '192.168.20.240','root','Rc123#@!', 'dayi',3306, 'utf-8'
    return host, user, password,database, port, charset


