import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# js与web自动化作业：以上操作均用python+selenium+js完成
# 如：在百度输入苹果手机，复制手机2个字，另外打开一个窗口为京东，在京东的搜索框中粘贴复制的手机，点击查找操作，再关闭京东，退出。
# 1：打开百度，在搜索框输入文本，选取部分文本赋值，另外打开一个窗口，
class Test0829():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
    def baidu(self):
        self.driver.get('https://www.baidu.com')
        ele = self.driver.find_element_by_id('kw')
        ele.send_keys('苹果 手机')
        time.sleep(1)
        ActionChains(self.driver).double_click(ele).perform()  # 双击可以选中后面词汇
        time.sleep(1)
        ele.send_keys(Keys.CONTROL, 'c')
        # 窗口的url自定义（淘宝），再粘贴复制的文本进行查找等操作，
        self.driver.execute_script('window.open("https://www.taobao.com/")')
        all = self.driver.window_handles
        self.driver.switch_to_window(all[-1])
        time.sleep(2)
        self.driver.find_element_by_class_name('search-combobox-input-wrap').send_keys(Keys.CONTROL, 'v')
        # js = 'document.getElementsByClassName("search-combobox-input-wrap").value="{}"'.format(Keys.CONTROL, 'v')
        # self.driver.execute_script(js)
        time.sleep(2)
        # 关闭新打开的窗口，退出。
        self.driver.close()
        time.sleep(1)
        self.driver.quit()
    def info(self,url):
        # 2：任意打开一个链接，用js获取url、hostname、port、title等值并进行输入
        self.driver.get(url)
        # url
        print('url:', self.driver.execute_script('return window.location.href'))
        # 域名信息
        print("域名信息:", self.driver.execute_script('return window.location.hostname'))
        # 协议
        print("协议:", self.driver.execute_script('return window.location.protocol'))
        # 标题
        print("标题信息:", self.driver.execute_script('return window.location.title'))
        self.driver.quit()
    def scroll(self):
        # 3：https://edit.newrank.cn/，控制非页面滚动条滑动
        self.driver.get('https://edit.newrank.cn/')
        # ele = self.driver.find_element_by_id('styleShow')
        # print(ele.scrollHeight)
        time.sleep(5)
        js_height = 'return document.getElementById("styleShow").scrollHeight'
        h = self.driver.execute_script(js_height)
        print(h)
        # self.driver.execute_script('document.getElementById("styleShow").scrollTop={}'.format(h))
        self.driver.execute_script('document.getElementById("styleShow").scrollTop=document.getElementById("styleShow")')
        time.sleep(2)
        self.driver.quit()

a = Test0829()
# a.baidu()
# a.info('https://www.baidu.com')
a.scroll()
# 课堂练习：
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com')
# # url信息
# print(driver.execute_script('return window.location.href'))
# # 域名信息
# print("域名信息:", driver.execute_script('return window.location.hostname'))
# # 协议
# print("协议:", driver.execute_script('return window.location.protocol'))
# # 页面路径或文件名
# print("路径:", driver.execute_script('return window.location.pathname'))
# time.sleep(2)
#
# js = 'location.assign("https://www.tmall.com")'
# driver.execute_script(js)
# time.sleep(2)
#
# js2 = 'location.replace("https://www.jd.com")'
# driver.execute_script(js2)
# driver.back() #  返回到上一个页面
# time.sleep(2)
# driver.quit()