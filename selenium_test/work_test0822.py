# selenium的三种等待方式作业：
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
# 1：对元素定位和操作进行封装，
#     要求实现：
#         1）可以找到任意元素，输入任意文本值；
def ele_text(driver,loc_type,loc_text,content):
    '''
    找到元素进行文本输入的方法
    :param loc_type: 元素的定位方式：By.id
    :param loc_text: 元素定位的属性值
    :param content: 文本输入的内容
    :return:
    '''
    driver.find_element(by=loc_type, value=loc_text).send_keys(content)
#         2）找到任意元素，进行点击操作；
def ele_click(driver,loc_type,loc_text):
    driver.find_element(by=loc_type, value=loc_text).click()
#         3）获取当前界面的title，并通过判断title来输出页面是否打开成功；
def ele_title(title):
    c_title = driver.title
    if c_title == title:
        print("title正确，打开成功！！")
    else:
        print("打开失败！")
#         4）获取当前的url，并通过判断url来输出页面是否打开成功
def url(url):
    c_url = driver.current_url
    if c_url == url:
        print("url正确，打开成功！！")
    else:
        print("打开失败")
#         5）对显示等待进行封装，
def wait_time(driver,timeout,loc_type,loc_value):
    webwait = WebDriverWait(driver, timeout)
    webwait.until(lambda x: driver.find_element(loc_type, value=loc_value))

# 2：对论坛进行脚本编写，地址http://49.233.108.117:3000/
#      要求实现：
#         1）进行登录操作
driver.get("http://49.233.108.117:3000/")
ele_click(driver, By.LINK_TEXT, "登录")
# 显示等待 输入文本
wait_time(driver, 10, By.ID, "name")
ele_text(driver, By.ID, "name", "test99")
ele_text(driver, By.ID, "pass", "123456")
ele_click(driver, By.CLASS_NAME, "span-primary")
url("http://49.233.108.117:3000/")
ele_title("CNode：Node.js专业中文社区")

#         2）进行发帖操作
#         要求调用第一题中封装的各种方法来实现登录操作和定位元素
wait_time(driver, 20, By.ID, "create_topic_btn")  # 等待按钮出现
ele_click(driver, By.ID, "create_topic_btn")
url("http://49.233.108.117:3000/topic/create")
#  选择板块
select = driver.find_element_by_id("tab-value")
se = Select(select)
se.select_by_value("share")  # 选择分享
ele_text(driver, By.ID, "title", "这是测试标题！")
#  todo 定位不到正文内容输入框
ele_click(driver, By.XPATH, '//*[@class="CodeMirror-scroll"]')
ele_text(driver, By.XPATH, '//*[@id="create_topic_form"]/fieldset/div/div/div[2]/div[1]/textarea', "主题内容")
time.sleep(2)
# driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# wait_time(driver, 10, By.CLASS_NAME, "editor_buttons")
ele_click(driver, By.XPATH, '//*[@id="create_topic_form"]/fieldset/div/div/div[4]/input')
wait_time(driver, 10, By.LINK_TEXT, "这是测试标题！")







