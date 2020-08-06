# 03 Python常用数据类型-字符串、列表、元祖的操作作业
# 一、字符串练习题：
# 1：有变量name = “aleX leNb “ 完成如下操作：
name = "aleX leNb "
#     移除 name 变量对应的值两边的空格,并输出处理结果
print(name.strip(" "))
#     判断 name 变量是否以 “al” 开头,并输出结果（用切片）
#print(name[:2] == "al")
print(name.startswith("al"))
#     判断name变量是否以”Nb”结尾,并输出结果（用切片）
print(name.endswith("Nb"))
#     将 name 变量对应的值中的 所有的”l” 替换为 “p”,并输出结果
print(name.replace("l", "p"))
#     将name变量对应的值中的第一个”l”替换成”p”,并输出结果
print(name.replace("l", "p", 1))
#     将 name 变量对应的值根据 所有的”l” 分割,并输出结果
print(name.split("l"))
#     将name变量对应的值根据第一个”l”分割,并输出结果
print(name.split("l", 1))
#     将 name 变量对应的值变大写,并输出结果
print(name.upper())
#     将 name 变量对应的值变小写,并输出结果
print(name.lower())
#     请输出 name 变量对应的值的第 2 个字符?
print(name[1:2])
#     请输出 name 变量对应的值的前 3 个字符?
print(name[:3])
#     请输出 name 变量对应的值的后 2 个字符?
print(name[-2:])


# 2：有字符串s = “123a4b5c”
s = "123a4b5c"
#     通过对s切片形成新的字符串 “123”
s1 = s[:3]
#     通过对s切片形成新的字符串 “a4b”
s2 = s[3:6]
#     通过对s切片形成字符串s5,s5 = “c”
s5 = s[-1]
#     通过对s切片形成字符串s6,s6 = “:2abc”
s6 = s[1::2]
print(s1, s2, s5, s6)

# 二、列表练习题：
# 1：写代码，有如下列表，按照要求实现每一个功能。
#     li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
#     计算列表的长度并输出
print(len(li))
#     请通过步长获取索引为偶数的所有值，并打印出获取后的列表
print(li[::2])
#     列表中追加元素”seven”,并输出添加后的列表
li.append("seven")
print(li)
#     请在列表的第1个位置插入元素”Tony”,并输出添加后的列表
li.insert(0, "Tony")
print(li)
#     请修改列表第2个位置的元素为”Kelly”,并输出修改后的列表
li[1] = "Kelly"
print(li)
#     请将列表的第3个位置的值改成 “太白”，并输出修改后的列表
li[2] = "太白"
print(li)
#     请将列表 l2=[1,”a”,3,4,”heart”] 的每一个元素追加到列表li中，并输出添加后的列表
l2 = [1, "a", 3, 4, "heart"]
li.extend(l2)
print(li)
#     请将字符串 s = “qwert”的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
s = "qwert"
li.extend(list(s))
print(li)
#     请删除列表中的元素”ritian”,并输出添加后的列表
li.remove("ritian")
print(li)
#     请删除列表中的第2个元素，并输出删除元素后的列表
li.pop(1)
print(li)
#     请删除列表中的第2至第4个元素，并输出删除元素后的列表
del li[1:4]
print(li)
# 2：写代码，有如下列表，利用切片实现每一个功能
#     li = [1, 3, 2, "a", 4, "b", 5,"c"]
li = [1, 3, 2, "a", 4, "b", 5, "c"]
#     通过对li列表的切片形成新的列表 [1,3,2]
print(li[:3])
#     通过对li列表的切片形成新的列表 [“a”,4,”b”]
print(li[3:6])
#     通过对li列表的切片形成新的列表 [1,2,4,5]
print(li[::2])
#     通过对li列表的切片形成新的列表 [3,”a”,”b”]
print(li[1:6:2])
#     通过对li列表的切片形成新的列表 [3,”a”,”b”,”c”]
print(li[1::2])
#     通过对li列表的切片形成新的列表 [“c”]
print(li[-1:])
#     通过对li列表的切片形成新的列表 [“b”,”a”,3]
li.reverse()
print(li[2::2])
# 3：写代码，有如下列表，按照要求实现每一个功能。
#     lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
#     将列表lis中的”k”变成大写，并打印列表。
print(str(lis[2]).upper())
#     将列表中的数字3变成字符串”100”
lis[1] = "100"
print(lis)
# print(li ="100")
#     将列表中的字符串”tt”变成数字 101
lis[3][2][1][0] = 101
print(lis)
#     在 “qwe”前面插入字符串：”火车头”
lis[3].insert(0, "火车头")
print(lis)