# -*- coding:utf-8 -*-
# @Time     :2020/9/30 15:20
# @Author     :liyuan
# @File      :get_mysql.py
# @Software  :PyCharm


import pymysql
from config.conf import *

def get_sql(sql):
    """

    :param sql:
    :return:
    """
    host, user, password,database, port, charset = sql_cof()
    db= pymysql.connect(host=host, user=user, password=password,database=database, port=port)
    cursor=db.cursor()
    cursor.execute(sql)
    data=cursor.fetchall()
    cursor.close()
    db.close()
    return data

print(get_sql('SELECT count(1) FROM t_talent_inf'))
