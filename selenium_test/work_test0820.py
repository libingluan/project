# 二：元素定位练习：
import random
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# 练习1：勾选下图中的所有的选项，包括复选框和单选框，文件：file1.html
driver = webdriver.Chrome()
driver.maximize_window()  # 最大化浏览器
# driver.get("file:///Users/libingluan/Downloads/python/huace/project-master/project/selenium_test/file1.html")
# time.sleep(5)
# selects = driver.find_elements_by_tag_name('input')
# for element in selects:
#     element.click()
#     time.sleep(2)
# time.sleep(3)
# driver.quit()
# 练习2：针对上面的案例(file.html)，我们只要选中复选框，针对单选框不做选中的操作，该如何实现？--可以查看课件中的截图
# elements = driver.find_elements_by_xpath('//input[@type="checkbox"]')
# print(elements)
# for element in elements:
#     element.click()
#     time.sleep(2)
# driver.quit()
eles = driver.find_element_by_tag_name('input')
for i in eles:
    if i.get_attribut('type') == "checkbox":
        i.click()
        time.sleep(1)
driver.quit()
# 练习3：进入百度新闻   http://news.baidu.com/
# driver.get('http://news.baidu.com')
# time.sleep(2)
# 第一问：定位热点要闻的一组标签，要求对每个标签执行点击操作，用定位一组元素的方式来实现         父标签》每一个子标签的规律
# elements = driver.find_elements_by_xpath('//*[@id="pane-news"]/div/ul/li/strong/a')
# for element in elements:
#     element.click()
#     time.sleep(1)
# driver.quit()
# 第二问：定位热点要闻的一组标签，只对第一条新闻进行点击操作，其他新闻则获取文本信息，输出文本信息 --选做题
# elements = driver.find_elements_by_xpath('//*[@id="pane-news"]/div/ul/li/strong/a')
# for i in range(len(elements)):
#     if i == 0:
#         elements[i].click()
#         time.sleep(1)
#     else:
#         print(elements[i].text)
#         time.sleep(1)
# driver.quit()
# 练习4:12306订票，url：https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc
# 操作流程：打开网址--设置出发地，目的地，出发日，发车时间，点击查询--可以查看课件中的截图
driver.get("https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc")
time.sleep(2)
# 点击输入框获取地址
# 出发地
driver.find_element_by_id("fromStationText").click()

driver.find_element_by_id("fromStationText").send_keys('广州\n')
# starts = driver.find_elements_by_xpath('//ul[@id="ul_list1"]/li')
# start = random.choice(starts)
# start.click()
# # 目的地
driver.find_element_by_id("toStationText").click()
driver.find_element_by_id("toStationText").send_keys('长沙\n')
# arrives = driver.find_elements_by_xpath('//ul[@id="ul_list1"]/li')
# random.choice(arrives).click()

driver.find_element_by_id("train_date").click()
time.sleep(2)
date = driver.find_element_by_xpath('/html/body/div[37]/div[2]/div[2]/div[1]/div')
date.click()
time.sleep(2)
# 时间
select = driver.find_element_by_id("cc_start_time")
#实例对象
se = Select(select)
se.select_by_visible_text("00:00--06:00")  # 文本
time.sleep(1)
se.select_by_index(2)   #从0开始
se.select_by_value("06001200")




#查询
driver.find_element_by_id("query_ticket").click()
driver.quit()