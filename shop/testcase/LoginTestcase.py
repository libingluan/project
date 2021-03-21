import unittest
from selenium import webdriver
import HTMLTestRunner
from shop.BasePage import Browser_init
from ddt import ddt, data, unpack, file_data


@ddt()
class LoginTestcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        #每个模块测试都只会打开一次浏览器和关闭一次浏览器
        print("执行多少用例都只需要打开一次浏览器")
        global driver #声明全局变量driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(20)

    @classmethod
    def tearDownClass(cls) -> None:

        print("执行后关闭")
        driver.quit()

    def setUp(self) -> None:
        #每个用例执行前都准备工作
        print("每个用例执行前都准备工作")
        # 进入
        # driver.get("http://shopxo.hctestedu.com/")
        # driver.find_element_by_link_text("登录").click()

    def tearDown(self) -> None:
        print("每个用例执行后复原")
        # driver.find_element_by_link_text("退出").click()

    # 登录模块的测试用例
    @data(('name1','123'),('name2','123'),('name3','123'))
    @unpack
    def testlogin01(self,name,pwd):
        self.login(driver,name,pwd)
        act_url = driver.current_url
        exp_url = "http://shopxo.hctestedu.com/index.php?s=/index/user/logininfo.html"
        self.assertTrue(act_url,exp_url)
    @file_data('../config/login.yaml')
    @unpack
    def testlogin02(self,name,pwd):
        self.login(driver,name,pwd)
        exit_ele = driver.find_elements_by_link_text("退出")
        ele_len = len(exit_ele)
        self.assertTrue(1,ele_len)

    # 多个不同的字段
    def test03(self,**kwargs):
        print(**kwargs)
        print("url",**kwargs["url"])




# class SearchTestcase(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:
#         # 每个模块测试都只会打开一次浏览器和关闭一次浏览器
#         print("执行多少用例都只需要打开一次浏览器")
#         global driver  # 声明全局变量driver
#         driver = webdriver.Chrome()
#         driver.implicitly_wait(20)
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         print("执行后关闭2")
#         driver.quit()
#
#     def setUp(self) -> None:
#         # 每个用例执行前都准备工作
#         print("每个用例执行前都准备工作")
#         # 进入
#         # driver.get("http://shopxo.hctestedu.com/")
#         # driver.find_element_by_link_text("登录").click()
#
#     def tearDown(self) -> None:
#         print("每个用例执行后复原2")
#     def test01(self):
#         # 不登录搜索
#         driver.get("http://shopxo.hctestedu.com/")
#         search(driver,"包包")
#
#     def test02(self):
#         #登录成功搜索手机
#         login(driver,"miya","Lbl123456")
#         search(driver, "手机")


if __name__ == '__main__':
    #unittest.main() # 执行所有类中以test开头都用例
    # 1创建一个测试套件
    suite =unittest.TestSuite()
    # 2指定用例
    # 2.1每次加一个
    # suite.addTest(LoginTestcase("testlogin01"))
    # suite.addTest(SearchTestcase("test01"))
    # 2.2一次添加一个列表
    # cases = [SearchTestcase("test01"),LoginTestcase("testlogin01")]
    # suite.addTests(cases)
    # 2.3 按模块执行
    loader = unittest.TestLoader()
    caselist=loader.loadTestsFromTestCase(LoginTestcase)
    suite.addTests(caselist)
    # suite.addTests(loader.loadTestsFromTestCase(LoginTestcase))
    # 3.执行套件：首先创建执行器，再用执行器执行套件
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=open("/Users/libingluan/Downloads/python/huace/project-master/project/web/report.html","wb"),
                          verbosity=2,
                          title="shop",
                          description="登录功能自动化")
    runner.run(suite)
