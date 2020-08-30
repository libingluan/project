# selenium的键盘和鼠标作业
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# 1：如何实现选中部分文本进行剪切和粘贴的操作？  可以以百度搜索为案例
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
ele = driver.find_element_by_id('kw')
ele.send_keys("selenium 教程")
time.sleep(1)
ActionChains(driver).double_click(ele).perform()
# ele.send_keys(Keys.CONTROL, 'a')
time.sleep(1)
ele.send_keys(Keys.CONTROL, 'X')
time.sleep(1)
ele.send_keys(Keys.CONTROL, 'V')
time.sleep(3)
driver.quit()
# 2：对selenium_webdriver操作.xmind总结文档补充完整，对于没有写上的点可以加上
# 3：查看下面附件，完成作业
# # 1) 打开携程网注册页面https://passport.ctrip.com/user/reg/home，要求点同意 滑动滑块验证
# driver.get('https://passport.ctrip.com/user/reg/home')
# # 判断是否存在，存在先点击同意
# agree = driver.find_element_by_xpath('//*[@id="agr_pop"]/div[3]/a[2]')
# time.sleep(2)
# if agree:
#     agree.click()
# time.sleep(1)
# drop_box = driver.find_element_by_xpath('//*[@id="slideCode"]/div[1]/div[2]')
# bar = driver.find_element_by_class_name('cpt-bg-bar')
# x = bar.location['x']
# y = bar.location['y']
# print(x, y)
# # 获取坐标拉不到最右边，直接输入比坐标大的数值
# ActionChains(driver).drag_and_drop_by_offset(drop_box, xoffset=300, yoffset=300).perform()
# time.sleep(2)
# driver.quit()

# # 2）打开淘宝，https://www.taobao.com/鼠标悬停在中国大陆，在点击中国台湾的操作
# driver.get("https://www.taobao.com/")
# #将 ActionChains进行实例化
# actionChain = ActionChains(driver)
# time.sleep(2)
# ele = driver.find_element_by_xpath('//*[@id="J_SiteNavBdL"]/li[1]')
# actionChain.move_to_element(ele).perform()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="J_SiteNavRegionList"]/li[4]').click()
# time.sleep(5)
# driver.quit()