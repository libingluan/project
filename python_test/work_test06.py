# 一、函数作业
# 1.写函数，接收两个数字参数，返回最大值
# 例如：
# 传入：10,20
# 返回：20
# def number(a,b):
#     if a > b:
#         print("较大的数值为：", a)
#     elif a == b:
#         print("数值相等")
#     else:
#         print("较大的数值为：", b)
# number(10,20)
# 2.写函数，获取传入列表的所有奇数位索引对应的元素，并将其作为新列表返回。
# 例如：
# 传入：[34,23,52,352,352,3523,5]
# 返回：[23,352,3523]
def numbe1(li):
    l2 = []
    # for i in range(1, len(li), 2):
    #     l2.append(li[i])
    # return l2
    for i in range(1, len(li)):
        if i % 2 != 0:
            l2.append(li[i])
    return l2
print(numbe1([34,23,52,352,352,3523,5]))
# 3.写函数，判断用户传入的对象（列表）长度是否大于5，如果大于5，那么仅保留前五个长度的内容并返回。不大于5返回本身。
# 例如：
# 传入1：[34,23,52,352,666,3523,5]   	               返回1：[34,23,52,352,666]
# 传入2：[34,23,52]     			返回2：[34,23,52]
def number2(li):
    if len(li) >= 5:
        print(li[:5])
    else:
        print(li)
number2([34,23,52])
number2([34,23,52,352,666,3523,5])
# 4.写函数，检查传入的字符串是否含有空字符串，返回结果，包含空字符串返回True，不包含返回False
# 例如：
# 传入："hello world"
# 返回：True
def hello(id):
    for i in id:
        #if i == " ":
        if i.isspace():
            return True
    return False
print(hello("helloworld"))
# 5.写函数，接收n个数字，分别写4个函数求n数字的和、差、商、积
# 求多个数的和
def add(*args):
    return sum(args)
print(add(1,2,3,6,10))

# 求多个数的差
def sub(*args):
    s = args[0]
    for i in range(1, len(args)):
        s -= args[i]
    return s
def sub(num,*args):
    s = num
    for i in range(len(args)):
        s -= args[i]
    return s
print(sub(10,5,2))
# 求多个数的积
def mul(*args):
    m = 1
    for i in args:
        m *= i
    print(m)
mul(10,5,2)
# 求多个数的商
def div(num,*args):
    s = num
    for i in range(len(args)):
        s /= args[i]
    return s
print(div(100,3,5))

# 6.(选做)实现学生管理系统,完成对学员的增,删,改,查和退出学生管理系统。
# 要求1：使用一个list用于保存学生的姓名。
# 要求2：输入0显示所有学员信息,1代表增加，2代表删除，3代表修改，4代表查询，exit代表退出学生管理系统。每一个功能定义一个自定义函数。界面如下：
# 系统界面如下：
# -----------------------欢迎进入V207班学生管理系统-----------------------------
# 请选择系统功能：
# 0:显示所有学员信息
# 1:添加一个学员信息
# 2:删除一个学员信息
# 3:修改一个学员信息
# 4:查询一个学员信息
# exit:退出学生管理系统
# (0)输入0后效果如下：
# 	0
# 	["那棵草","下个路口见"..]
# (1)输入1后效果如下：
# 	1
# 	请输入增加人的姓名：南一
# 	["那棵草","下个路口见",'南一'..]
# (2)输入2后效果如下：
# 	2
# 	请输入删除人的姓名：南一
# 	["那棵草","下个路口见"..]
# (3)输入3后效果如下：<注意：如果list中没有这个学员则打印：V207班没有这个学员>
# 	3
# 	请输入需要修改人的姓名：下个路口见
# 	请输入需要修改后的姓名：小蓝紫
# 	["那棵草","小蓝紫"..]
# (4)输入4后效果如下：<注意：如果list中没有这个学员则打印：V207班没有这个学员>
# 	请输入查询人的姓名：那棵草
# 	那棵草在座位号(0<下标>)的位置。
# (5)输入exit后效果如下：
# 	exit
# 	欢迎使用V207的学生管理系统，下次再见。
# 二.模块作业：
#  1： 将1-5题中定义的函数放在demo.py文件中，在module_demo.py文件中导入demo.py文件，并调用文件中的所有函数。
#  2：熟悉time,datetime,calendar模块中常用的方法、转换、截取等操作，熟悉上课讲的内容
