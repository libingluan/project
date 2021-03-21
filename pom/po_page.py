from selenium.webdriver.common.by import By

from pom.base import Browser_init

class SearchPage(Browser_init):
    #子类可以直接调用父类的公有方法和属性
    def __init__(self,driver):
        self.driver = driver

    #抽离元素属性值
    # search_input = "kw"
    # search_btn = "su"

    search_input = (By.ID, "KW")
    search_btn = (By.ID, "su")

    def input_search(self,txt):
        self.driver.find_element(*SearchPage.search_input).send_keys(txt)

    def click_search(self):
        self.driver.find_element(*SearchPage.search_btn).click

