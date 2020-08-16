
# 写一个装饰器具体功能如下：
# 	每个函数的执行名称
# 	每个函数执行的当前时间
# 	每个函数的执行所用时间
import functools
import time


def log(func):
    @functools.wraps(func)
    def wrapper(*args):
        print(args)
        start_time = time.time()
        print("开始执行函数：%s" %func.__name__,start_time)
        print("函数开始执行的时间为：", start_time)
        # 执行原始函数
        c = func(*args)
        end_time = time.time()
        print("执行{}函数结束---" .format(func.__name__,end_time))
        print("函数执行结束时间为：", end_time)
        print("函数{}的执行所用时间为{}".format(func.__name__, end_time-start_time))
        return c
    return wrapper


@log
def test(*args):
    lis = list(map(lambda x: x*x, args))
    print(lis)
    print("这是一个执行的原始函数")

li= [1,2,3,4,5]
test(*li)