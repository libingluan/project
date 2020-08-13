import math
# 一、编写一个学生类，有姓名，年龄，性别，英语成绩，数学成绩，语文成绩，方法：求总分，平均分，以及打印学生的信息。
# 类：学生（student）
# 属性：姓名（name）
# 年龄（age）
# 性别（gender）
# 英语成绩（English_score）
# 数学成绩（math_score）
# 语文成绩（chinese_score）
# 总成绩（total_score）
# 平均成绩（avg_score）s
class Student():
    def __init__(self, name, age, gender, English_score, math_score, chinese_score):
        self.name = name
        self.age = age
        self.gender = gender
        self.English_score = English_score
        self.math_score = math_score
        self.chinese_score = chinese_score
    def total_score(self):
        total_score = self.English_score + self.math_score + self.chinese_score
        return  total_score
    def avg_score(self):
        avg = self.total_score()/3
        return avg
    def student_info(self):
        print('''学生的信息为：
        姓名：{}
        年龄：{}
        性别：{}
        英语成绩：{}
        数学成绩：{}
        英语成绩：{}
        总成绩：{}
        平均成绩：{}
        '''.format(self.name, self.age, self.gender, self.English_score, self.math_score, self.chinese_score,
                   self.total_score(), self.avg_score()))
zs = Student("张三",18,"男",100,90,80)
zs.student_info()

# 二、为"无名的粉"写一个类WuMingFen，有三个属性 面码:String theMa  粉的分量(两) int quantity  是否带汤 boolean likeSoup
# 要求：
# 1）写一个构造方法 分别给三个属性赋值。构造出一个WuMingFen类的对象(酸辣面码、2两、带汤)，
# 2）写一个普通方法check()打印对象的三个属性。通过对象调用此方法。
class WuMingFen():
    def __init__(self, String_theMa, int_quantity, boolean_likeSoup):
        self.String_theMa = String_theMa
        self.int_quantity = int_quantity
        self.boolean_likeSoup = boolean_likeSoup
    def check(self):
        print('''无名粉的信息：
        面码：{}
        粉的分量（两）:{}两
        是否带汤：{}
        '''.format(self.String_theMa, self.int_quantity, self.boolean_likeSoup))
F = WuMingFen("酸辣面码",2,"带汤")
F.check()
# 三、定义一“圆”Cirlcle类，圆心为“点”Point类，构造一圆，求圆的周长和面积，并判断某点与圆的关系。
# 某点与圆心的距离大于半径，在圆外；=r,在圆上；<r，在圆内
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Cirlcle():
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def perimeter(self):
        return 2*math.pi*self.radius

    def area(self):
        return math.pi*self.radius**2

    def check_point(self, point_x, point_y):
        d = (point_x-self.center.x)**2 + (point_y-self.center.y)**2
        if d > self.radius**2:
            print("某点在圆外")
        elif d == self.radius**2:
            print("某点在圆上")
        else:
            print("某点在圆内")
# 圆心的实例化
c = Point(0,0)
# 实例化一个圆
cir = Cirlcle(c, 5)
print("周长：", cir.perimeter())
print("面积：", cir.area())
cir.check_point(1, 1)
cir.check_point(5, 6)
cir.check_point(0, 5)

