#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021-03-20 20:13
# @Author : libingluan
# @File : 接口关联.py
# @Software: PyCharm

import requests

# z站站查询
# url_1 = "https://api.binstd.com/train/station2s"
# params_1 = {"appkey": "60e313d2015a1f6f",
#         "start": "长沙",
#         "end": "广州",}
# res = requests.get(url_1, params=params_1)
# print(res.text)
# #1、从站站查询接口获取所有车次信息，2、遍历所有的车次
# list=res.json()['result']['list']
# tranin_list=[]
# for i in range(len(list)):
#     tranin_list.append(list[i]['trainno'])
# print(tranin_list)
#
# # 车次查询
# url_2 = "https://api.binstd.com/train/line"
# for i in tranin_list:
#      params_2 = {"appkey": "60e313d2015a1f6f",
#         "trainno": i}
#      res2 = requests.get(url_2, params=params_2)
#      print(res2.text)


# cookie
#12306火车票查询
# url_3 = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2021-03-20&leftTicketDTO.from_station=GZQ&leftTicketDTO.to_station=CSQ&purpose_codes=ADULT"
# header = {
#     "Cookie": "_uab_collina=159815991483483595204323; JSESSIONID=1502E10F34D3C760D959572AC98ABE2E; _jc_save_wfdc_flag=dc; BIGipServerotn=3973513482.64545.0000; RAIL_EXPIRATION=1616504327992; RAIL_DEVICEID=rSrEpm6pCHbJTFNt7TOwZh50G07P_BSSaeZ3_PXokAJbOMXZl6mQa5-ES7LMb58RlvEMcuxhwb8FwMcL79m5jZBzQrr9e5_7qgzne5Fbj4h7ZdQ_Aatc19H0bZYxZYao3MggQwIJsA-nsxy0NmY-rcEW0nZkgcO9; BIGipServerpassport=954728714.50215.0000; route=495c805987d0f5c8c84b14f60212447d; _jc_save_fromStation=%u5E7F%u5DDE%2CGZQ; _jc_save_toStation=%u957F%u6C99%2CCSQ; _jc_save_fromDate=2021-03-20; _jc_save_toDate=2021-03-20"
# }
# res3 = requests.get(url_3, headers=header)
# res3.encoding("utf-8")
# print(res3.text)

# cookie-session