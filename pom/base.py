

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

class Browser_init():
    # 1 解决浏览器driver问题
    #无论是po层还是base都是用测试用例
    def __init__(self,driver):
        self.driver= driver

        #继承：
        #父类有构造方法，子类没有构造方法，示例化子类对象时，自动调用父类的构造方法

        # 2、封装常见的方法：打开浏览器、打开url、元素定位、元素等待、输入

        def Wait_ele(self,locator,time=10):
            # locator是元组定位
            wait = WebDriverWait(self.driver,time)
            ele = wait.until(EC.presence_of_element_locator(locator),message=" 没有该元素")
            return ele

