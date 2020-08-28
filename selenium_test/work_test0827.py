# selenium的键盘和鼠标作业
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 1：如何实现选中部分文本进行剪切和粘贴的操作？  可以以百度搜索为案例
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys("selenium 教程")

# 2：对selenium_webdriver操作.xmind总结文档补充完整，对于没有写上的点可以加上
# 3：查看下面附件，完成作业