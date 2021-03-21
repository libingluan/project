#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021-03-18 21:20
# @Author : libingluan
# @File : get请求.py
# @Software: PyCharm


import requests


# 一、get请求
# 发送请求必须要素：url 方法、【入参】【请求头参数】
url = "https://www.baidu.com"
# res = requests.get(url)
res=requests.request('GET',url)
print(res, type(res))
print(res.text)
print(res.encoding)
res.encoding = 'utf-8'


# 发送请求，将url和参数拆分
# 例子1：https://www.baidu.com?id=1001
# url = "https://www.baidu.com"
# data = {"id": 1001}
# res = requests.request("get", url, params=data)
#
# # 例子2：https://www.baidu.com?id=1001,1002
# url = "https://www.baidu.com"
# data = {"id": "1001,1002"}
# res = requests.request("get", url, params=data)


# 二、post请求
url1 = "http://api.test.zhulogic.com/designer_api/account/login_quick"
data={"phone":137,
      "code":1234,
      "unionid":"",
      "messagetType":3,
      "channel":"zhulogic",
      }
head = {"Content_Type":"application/json"}
# json格式实现方法1
res = requests.request("post",url=url1,json=data,headers=head)
# 方式2
# import json
# newdata = json.dumps(data)  # 将对象转换成json
# res = requests.post(url1,data=newdata,headers=head)

print(data, type(data))
# print(newdata, type(newdata))

print(res.text)
print(res.json())



