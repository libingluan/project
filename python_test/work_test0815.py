# # 写一个日志模块类：
# # 1.添加 俩个不同的处理器
# # 2.不同的处理器设置不同的日志等级
# # 3.不同的处理器设置不同的输出格式
# # （要求：不看录播中老师写的 类，自己独立写出来
# import logging
# import time
# class log_object():
#     def __init__(self):
#         '''
#          定制日志器对象
#          格式器
#          文件名称
#         '''
#         self.logger = logging.getLogger()  # 创建日志器
#         self.logger.setLevel(level=logging.DEBUG)  #创建日志器等级
#         self.f = ' %(asctime)s --%(filename)s--%(levelname)s ->>>>%(message)s '
#         self.format = logging.Formatter(fmt=self.f)  # 创建格式器
#         self.file = './test{}.log'.format(time.time())
#
#     def add_StreamHandle(self):
#         # 添加控制台处理器\- 添加格式器、添加等级
#         hand = logging.StreamHandler()
#         hand.setFormatter(self.format)
#         hand.setLevel(level=logging.DEBUG)
#         self.logger.addHandler(hand)
#     def add_FileHandler(self):
#         # 添加 文件处理器\- 添加格式器、添加等级
#         file = logging.FileHandler(filename=self.file, encoding='utf-8')
#         file.setFormatter(self.format)
#         file.setLevel(level=logging.DEBUG)
#         self.logger.addHandler(file)
#
#     def get_logger(self):
#         '''
#         返回日志器
#         :return:
#         '''
#         self.add_StreamHandle()
#         self.add_FileHandler()
#         return self.logger
# if __name__ == '__main__':
#     log = log_object().get_logger()
#     log.debug("这是debug")
#     log.info("这是info")
#     log.warning("这是warning")
#     log.error("这是error")
#     log.critical("这是critical")
#
# Python群发一个excel表格中的所有联系人的邮件
# 1.多个sheet表格依次发送所有的邮件
# 2.每个邮件的内容不一样
import openpyxl
# list = [["657367560@qq.com", "测试内容11"],["miya657367560@163.com", "测试内容222"],["miya1114@126.com", "测试内容333"],]
# # 创建一个文件
# book = openpyxl.workbook
# sheet1 = book["Sheet1"]
# for i in list:
#     sheet1.append(i)
# book.save("email_info.xlsx")