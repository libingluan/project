# 自动化常见操作作业：
import time
from selenium import webdriver
class Opts_handle():
    def __init__(self):
        # driver = webdriver.Chrome()
        opts = webdriver.ChromeOptions()
        opts.headless = True
        self.driver = webdriver.Chrome(options=opts)
        self.driver.maximize_window()
    def open_handle(self,url):
        # 作业一：
        # 1、进入百度视频   http://v.baidu.com/?fr=bd  首页
        self.driver.get(url)
        # 2、获取当前窗口的句柄
        shouye_handle = self.driver.current_window_handle
        self.driver.implicitly_wait(10)
        # 3、打开新的链接
        self.driver.find_element_by_id('new-bdvSearchInput').send_keys("以家人之名")
        self.driver.find_element_by_id('new-bdvSearchBtn').click()
        # 4、获取所有的句柄
        all_handles = self.driver.window_handles
        # 5、切换句柄到新的链接窗口
        self.driver.switch_to_window(all_handles[-1])
        # 6、通过打印新窗口的title来验证是否切换成功
        print(self.driver.title)
        # 7、关闭新的窗口，切换句柄到首页
        self.driver.close()
        self.driver.implicitly_wait(2)
        self.driver.switch_to_window(shouye_handle)
        # 8、通过打印首页的title来验证是否切换成功
        print(self.driver.title)
        self.driver.quit()
    def baidu_news(self,url2):
        # 作业二：
        # 在百度新闻页面，定位到一组标签，打开所有的链接，获取所有句柄，如果句柄与当前句柄不一致，则将不一致的窗口的标题打印出来
        self.driver.get(url2)
        # 获取首页到句柄
        first_handle = self.driver.current_window_handle
        elements = self.driver.find_elements_by_xpath('//*[@id="pane-news"]/div/ul/li')
        for element in elements:
            element.click()
            all_handle = self.driver.window_handles   # 获取所有都句柄信息
            self.driver.switch_to_window(all_handle[-1])  # 切换到最新打开到窗口
            current_handle = self.driver.current_window_handle
            if first_handle != current_handle:
                print(self.driver.title)
            self.driver.switch_to_window(all_handle[0])  # 回到第一个窗口
        self.driver.quit()
    def QQemail(self,url3):
        # 作业三：
        # 1、进入QQ邮箱  https://mail.qq.com/cgi-bin/loginpage
        # 2、输入错误用户名和密码，点击登录
        # 3、点击企业邮箱
        self.driver.get(url3)
        self.driver.implicitly_wait(2)
        # 定位到iframe元素并进入
        self.driver.switch_to_frame("login_frame")
        # 判断是否存在切换账户密码登录到按钮，存在先进入登录页面
        name = self.driver.find_element_by_id("switcher_plogin")
        if name:
            name.click()
        self.driver.implicitly_wait(5)
        # 获取账户密码登录
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="u"]').send_keys("657367560@qq.com")
        self.driver.find_element_by_xpath('//*[@id="p"]').send_keys("123456")
        # 点击登录
        self.driver.find_element_by_id('login_button').click()
        # 跳出iframe
        self.driver.switch_to_default_content()
        # 点击企业邮箱
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div/a[4]").click()
        print(self.driver.title)
        time.sleep(3)
        self.driver.quit()
# 作业四：
# 以上作业一到作业三都要用无头模式来运行，自行定义输出文本来判断脚本运行结果。
a = Opts_handle()
a.open_handle("http://v.baidu.com/?fr=bd")
a.baidu_news('http://news.baidu.com/')
a.QQemail('https://mail.qq.com/cgi-bin/loginpage')