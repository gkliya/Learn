# -*- coding:utf-8 -*-
# @Time     :2020/10/2 16:43
# @Author     :liyuan
# @File      :test_body.py
# @Software  :PyCharm

import requests
import re

"""
断言，自动检查看返回的结果是否跟预期的一致，用assert
主要检查返回的状态码，返回body里面的信息，还有数据库保存的结果的检查
"""

url = 'https://search.51job.com/list/030800,000000,0000,00,9,99,%25E8%25BD%25AF%25E4%25BB%25B6%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}
res = requests.get(url=url, headers=headers)
company_url = re.findall('"company_href":"([^(")]+?)","company_name":"东莞时力电子科技有限公司"', res.text)[0].replace('\\', '')
print(company_url)
company_message = requests.get(url=company_url, headers=headers)
company_message.encoding = 'gbk'
print(company_message.text)
# def test_huoche():
#     url= 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2020-10-02&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SZQ&purpose_codes=ADULT'
#     headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
#              'Cookie': '_uab_collina=160163393687599050467362; JSESSIONID=8708E9F18DD472F750B30468EE37C965; BIGipServerotn=619708938.38945.0000; BIGipServerpool_passport=199492106.50215.0000; RAIL_EXPIRATION=1601914650953; RAIL_DEVICEID=VX8Gt_Qx6hjTyP92XuQNi3Tt0a8UCeXO0D56WgOQg1ziPcjDVyKVCdLi6fJ6Vcpz7BzZ_JFck9Z0-RidIecoekUynDk8pwklY6DR7EEjvmYhWdIi3nvKvZUcjw4FGFtUffwxMBhGCajigCw63vptuIip6ESTt-xe; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u6DF1%u5733%2CSZQ; _jc_save_fromDate=2020-10-02; _jc_save_toDate=2020-10-02; _jc_save_wfdc_flag=dc'
#              }
#     res=requests.get(url=url,headers=headers)
#     # print(res.json()['data']['map'])
#     assert res.json()['data']['map']['SZQ'] == '深圳'


