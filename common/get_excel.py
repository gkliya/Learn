# -*- coding:utf-8 -*-
# @Time     :2020/9/30 13:57
# @Author     :liyuan
# @File      :get_excel.py
# @Software  :PyCharm


import xlrd

excel = xlrd.open_workbook('../testdata/username.xlsx')  # 地址用相对路径，不用绝对路径
table = excel.sheets()[0]


def get_excel_row(row):
    return table.cell_value(row,1), table.cell_value(row,2)

def get_excel_nrows():
    return table.nrows