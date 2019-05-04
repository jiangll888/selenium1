# encoding:utf-8
from base.base_page import BasePage
from base.get_element import GetElement
from selenium import webdriver
from config import settings
from page.login_page import LoginPage
import time

class HomePage(BasePage):
    def __init__(self,driver,url):
        super(HomePage,self).__init__(driver,url)
        self.get_ele = GetElement(driver)

    def get_enter_album_element(self):
        return self.get_ele.get_element("enter_aibum","home_element")

    def enter_album(self):
        self.click_element(self.get_enter_album_element())


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path=settings.CHROME_PATH)
    l = LoginPage(driver, settings.URL)
    l.login("jiangliulin@163.com", "baimaonv08340822")
    h = HomePage(driver, settings.URL)
    h.enter_album()
