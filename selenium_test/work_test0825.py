# 自动化常见操作作业：
import time

from selenium import webdriver
# driver = webdriver.Chrome()
opts = webdriver.ChromeOptions()
opts.headless = True
driver = webdriver.Chrome(options=opts)
driver.maximize_window()
# 作业一：
# 1、进入百度视频   http://v.baidu.com/?fr=bd  首页
# driver.get('http://v.baidu.com/?fr=bd')
# # 2、获取当前窗口的句柄
# shouye_handle = driver.current_window_handle
# driver.implicitly_wait(10)
# # 3、打开新的链接
# driver.find_element_by_id('new-bdvSearchInput').send_keys("以家人之名")
# driver.find_element_by_id('new-bdvSearchBtn').click()
# # 4、获取所有的句柄
# all_handles = driver.window_handles
# # 5、切换句柄到新的链接窗口
# driver.switch_to_window(all_handles[-1])
# # 6、通过打印新窗口的title来验证是否切换成功
# print(driver.title)
# # 7、关闭新的窗口，切换句柄到首页
# driver.close()
# driver.implicitly_wait(2)
# driver.switch_to_window(shouye_handle)
# # 8、通过打印首页的title来验证是否切换成功
# print(driver.title)
# driver.quit()
# 作业
# 作业二：
# 在百度新闻页面，定位到一组标签，打开所有的链接，获取所有句柄，如果句柄与当前句柄不一致，则将不一致的窗口的标题打印出来
# driver.get("http://news.baidu.com/")
# # 获取首页到句柄
# first_handle = driver.current_window_handle
# elements = driver.find_elements_by_xpath('//*[@id="pane-news"]/div/ul/li')
# for element in elements:
#     element.click()
#     all_handle = driver.window_handles   # 获取所有都句柄信息
#     driver.switch_to_window(all_handle[-1])  # 切换到最新打开到窗口
#     current_handle = driver.current_window_handle
#     if first_handle != current_handle:
#         print(driver.title)
#     driver.switch_to_window(all_handle[0])  # 回到第一个窗口
# driver.quit()
# 作业三：
# 1、进入QQ邮箱  https://mail.qq.com/cgi-bin/loginpage
# 2、输入错误用户名和密码，点击登录
# 3、点击企业邮箱
driver.get("https://mail.qq.com/cgi-bin/loginpage")
driver.implicitly_wait(2)
# 定位到iframe元素并进入
driver.switch_to_frame("login_frame")
# 判断是否存在切换账户密码登录到按钮，存在先进入登录页面
name = driver.find_element_by_id("switcher_plogin")
if name:
    name.click()
driver.implicitly_wait(5)
# 获取账户密码登录
time.sleep(3)
driver.find_element_by_xpath('//*[@id="u"]').send_keys("657367560@qq.com")
driver.find_element_by_xpath('//*[@id="p"]').send_keys("123456")
# 点击登录
driver.find_element_by_id('login_button').click()
# 跳出iframe
driver.switch_to_default_content()
# 点击企业邮箱
driver.find_element_by_xpath("/html/body/div/div[1]/div/a[4]").click()
print(driver.title)
time.sleep(3)
driver.quit()
# 作业四：
# 以上作业一到作业三都要用无头模式来运行，自行定义输出文本来判断脚本运行结果。
