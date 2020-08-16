# 写一个日志模块类：
# 1.添加 俩个不同的处理器
# 2.不同的处理器设置不同的日志等级
# 3.不同的处理器设置不同的输出格式
# （要求：不看录播中老师写的 类，自己独立写出来
import logging

# 创建日志器
import time

# logger = logging.getLogger()
# # 设置日志的级别
# logger.setLevel(logging.DEBUG)
#
# # 创建格式器
# f1 = logging.Formatter(fmt='%(asctime)s-- %(filename)s --%(lineno)d--%(levelname)s->>>>>>%(message)s ')
# f2 = logging.Formatter(fmt='%(asctime)s--->>>>>>%(message)s ')
# # 创建控制台-处理器
# hand = logging.StreamHandler()  # 实例化对象
# file = logging.FileHandler(filename='./filename.log', encoding='utf-8')
#
# # 控制台设置输出格式
# hand.setFormatter(f2)  # 调用对象的方法
# file.setFormatter(f1)
# # 设置日志等级
# hand.setLevel(level=logging.DEBUG)
# file.setLevel(level=logging.WARNING)
#
# # 添加处理器
# logger.addHandler(hand)
# logger.addHandler(file)
#
# logger.debug("这是debug")
# logger.info("这是info")
# logger.warning("这是warning")
# logger.error("这是error")



# 封装日志类
class log_object():
    def __init__(self):
        '''
        定义日志器对象
        格式器
        文件名称
        '''
        self.logger = logging.getLogger()
        self.logger.setLevel(level=logging.DEBUG)
        self.f = '%(asctime)s-- %(filename)s --%(lineno)d--%(levelname)s->>>>>>%(message)s '
        self.formatter = logging.Formatter(fmt=self.f)
        self.log_name = './test{}.log'.format(time.time)

    def add_StreamHandler(self):
        hand = logging.StreamHandler()
        hand.setLevel(level=logging.DEBUG)
        hand.setFormatter(self.formatter)
        self.logger.addHandler(hand)

    def get_log(self):
        '返回日志器'
        self.add_StreamHandler()
        return self.logger

if __name__ == '__main__':
    alog = log_object().get_log()
    alog.debug("这是debug")
    alog.info("这是info")
    alog.warning("这是warning")
    alog.error("这是error")