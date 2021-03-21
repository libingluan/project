from selenium import webdriver
import unittest
from pom.po_page import SearchPage
import ddt

class TestcaseBaidu(unittest.TestCase):
    def setUp(self) -> None:
        driver = webdriver.Chrome()
        driver.get("https://www.baidu.com")
        driver.implicitly_wait(10)
        self.baidu = SearchPage(driver)  # 实例化

    def tearDown(self) -> None:
        print("单个用例结束")


    def test01(self):
        self.baidu.input_search("自动化测试")
        self.baidu.click_search()

    def test02(self):
        pass




if __name__ == '__main__':
    unittest.main()