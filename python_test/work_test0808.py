# 一、摆放家具
# 需求：
# 1）房子有户型，总面积和家具名称列表
# 	新房子没有任何的家具
# 2）家具有名字和占地面积，其中
# 	床：占4平米
# 	衣柜：占2平面
# 	餐桌：占1.5平米
# 3）将以上三件家具添加到房子中
# 4）打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
# 创建家具类
class Furniture():
    def __init__(self,name,area):
        self.name = name
        self.area = area

# 创建房子的类 ，属性 户型、总面积、剩余面积、家具列表,方法 添加家具、打印房子
class House():
    def __init__(self,type,total_area):
        self.type = type
        self.total_area = total_area
        self.free_area = total_area
        self.furniture = []

    def newHouse(self):
        print("新房子户型：{},占地面积：{},家具：{}".format(self.type, self.total_area, self.free_area, self.furniture))

    def add_furniture(self,items):
        if self.free_area > items.area:
            self.furniture.append(items.name)
            self.free_area -= items.area
            print("房子户型：{},占地面积：{},剩余面积：{},家具：{}".format(self.type, self.total_area, self.free_area, self.furniture))
        else:
            print ("房间没有剩余空间可以添加家具")

bed = Furniture("床", 4)
table = Furniture("桌子", 1.5)
closet = Furniture("衣柜", 2)
house = House("3房2室", 20)
house.newHouse()
house.add_furniture(bed)
house.add_furniture(table)
house.add_furniture(closet)

# 二、需求：
# 	1）士兵瑞恩有一把AK47
# 	2）士兵可以开火(士兵开火扣动的是扳机)
# 	3）枪 能够 发射子弹(把子弹发射出去)
# 	4）枪 能够 装填子弹 --增加子弹的数量
# 创建枪的类  属性：名字 子弹  方法:装子弹、发射子弹
class Gun():
    def __init__(self, model, bullet=0):
        self.model = model
        self.bullet = bullet
    def add_bullet(self, count):
        self.bullet += count
        print("装子弹成功，数量为：", self.bullet)
    def shoot(self):
        if self.bullet <= 0:
            print("没有子弹请先装子弹！")
        else:
            print("biubiu....")
            self.bullet -= 1
            print("发射子弹成功，剩余子弹：", self.bullet)

# 创建士兵类  属性：名字、是否有枪  方法：开火
class Soldier():
    def __init__(self, name, gun=None): # gun枪的实例对象
        self.name = name
        self.gun = gun
        print("{}持有一把{}型号的枪".format(self.name, self.gun.model))
    def fire(self,count):
        if self.gun == None:
            print("没有枪")
        else:
            self.gun.add_bullet(count)
            self.gun.shoot()
            print("士兵{}子弹发射出去成功,".format(self.name))

gun = Gun("AK47", 30)
soldier = Soldier("瑞恩", gun)
soldier.fire(3)