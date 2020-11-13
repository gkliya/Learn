# -*- coding:utf-8 -*-
# @Time     :2020/10/2 21:24
# @Author     :liyuan
# @File      :run_all_cases.py
# @Software  :PyCharm

import pytest

if __name__ == '__main__':
    #单个文件运行，地址要用相对路径
    # pytest.main(['../test_case/test_add_park.py'])
    #多个文件运行，添加多个文件路径的地址
    # pytest.main(['../test_case/test_case01.py','../test_case/test_case02.py'])
    #整个目录 '--html=../report/report.html','junitxml=../report/report.xml',
    pytest.main(['../test_case','--alluredir','../report/reportallure/'])
    #命令allure generate ./reportallure/ -o ./reporthtml/ --clean
