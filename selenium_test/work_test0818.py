
# 实例对象 打开浏览器
# 打开网页  get
# 刷新  refresh
# 前进  forward
# 后退 back
# 截图 get_screenshot_as_file(slef,filename)
# 退出  close 关闭当前窗口  quit  关闭浏览器 停止驱动


from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")
# 等待1s
time.sleep(1)
driver.get_screenshot_as_file(filename="baidu.png")
# 刷新页面
driver.refresh()
# 打开淘宝首页
driver.get("https://www.taobao.com")
time.sleep(1)
driver.get_screenshot_as_file(filename="taobao.png")
#  后退
driver.back()
time.sleep(1)
# 前进
driver.forward()
time.sleep(1)
# 关闭浏览器
driver.quit()
