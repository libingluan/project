# 一：元祖练习题：判断是否可以实现，如果可以请写代码实现。
#     li = ["alex",[11,22,(88,99,100,),33] "WuSir", ("ritian", "barry",), "wenzhou"]
li = ["alex", [11, 22, (88, 99, 100,), 33], "WuSir", ("ritian", "barry",), "wenzhou"]
#     1：请将 "WuSir" 修改成 "吴彦祖"
li[2] = "吴彦祖"
print(li)
#     2：请将 ("ritian", "barry",) 修改为 ['日天','日地']
li[3] = ['日天', '日地']
print(li)
#     3： 请将 88 修改为 87
# 元组不能被修改
#     4： 请将 "wenzhou" 删除，然后再在列表第0个索引位置插入 "周周"
li.pop(-1)
li.insert(0, "周周")
print(li)
# 二、字典练习题：
# 1：根据需求写代码
#      dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
dic = {'k1': "v1", "k2": "v2", "k3": [11, 22, 33]}
#      请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
dic["K4"] = "V4"
print(dic)
#      请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
dic['k1'] = "alex"
print(dic)
#      请在k3对应的值中追加一个元素 44，输出修改后的字典
dic["k3"] = [11, 22, 33, 44]
print(dic)
#      请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
dic["k3"].insert(0, 18)
print(dic)
# 2：根据需求写代码
dic1 = {'name': ['alex', 2, 3, 5],
        'job': 'teacher',
        'oldboy': {'alex': ['python1', 'python2', 100]}
      }
#      1，将name对应的列表追加一个元素’wusir’。
dic1["name"].append("wusir")
print(dic1)
#      2，将name对应的列表中的alex首字母大写。
dic1["name"][0] = "Alex"
print(dic1)
#      3，oldboy对应的字典加一个键值对’老男孩’,’linux’。
dic1["oldboy"]["老男孩"] = "linux"
print(dic1)
#      4，将oldboy对应的字典中的alex对应的列表中的python2删除
dic1["oldboy"]["alex"].pop(1)
print(dic1)
# 三：集合练习题
# 1：[‘taobao’,'jingdong','alibaba','baidu','taobao']对元素去重复
# 2：分别有两个集合{1,2,1,3,4,5,6,7}，{1,2,3,8,9,7,10}，求两个集合的差集、并集、交集
# 四、格式化输出练习题：
# 1：题目：通过控制台获取你的相关信息（包括下面内容），对自己进行自我介绍，
# 要求使用上面两种方式来实现：
# 	name 	姓名
# 	age		年龄
# 	work_address	工作地
# 	hobby	爱好
# 	all_salary	年收入
# 	work_years	工作年限