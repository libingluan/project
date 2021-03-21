from selenium import webdriver
#hub的启动方式  命令行启动


# robotframe  自带多线程同时运行  同时运行100个用例放在100个node   -num
# pytest 多线程同时运行   -n
def test01():
    ds = {'platform': 'ANY','browserName': "chrome",}
    driver = webdriver.Remote('http://192.168.1.101:5588/wd/hub',desired_capabilities=ds)
    driver.get("https://www.baidu.com")
    driver.quit()

def test02():
    ds = {'platform': 'ANY','browserName': "firefox",}
    driver = webdriver.Remote('http://192.168.1.101:5599/wd/hub',desired_capabilities=ds)
    driver.get("https://www.baidu.com")
    driver.quit()

#pytest work_test0905.py -n 2
