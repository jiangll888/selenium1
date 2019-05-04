from base.base_page import BasePage
from base.get_element import GetElement
from selenium import webdriver
from config import settings

class LoginPage(BasePage):
    def __init__(self,driver,url):
        super(LoginPage,self).__init__(driver,url)
        self.get_ele = GetElement(driver)

    def get_username_element(self):
        return self.get_ele.get_element("username","login_element")

    def get_password_element(self):
        return self.get_ele.get_element("password","login_element")

    def get_login_btn_element(self):
        return self.get_ele.get_element("login_btn","login_element")

    def get_frame1_element(self):
        return self.get_ele.get_element("iframe1","login_element")

    def get_frame2_element(self):
        return self.get_ele.get_element("iframe2","login_element")

    def login(self,*args):
        self.open()
        self.switch_iframe(self.get_frame1_element())
        self.switch_iframe(self.get_frame2_element())
        self.send_msg(self.get_username_element(),args[0])
        self.send_msg(self.get_password_element(),args[1])
        self.click_element(self.get_login_btn_element())
        self.switch_iframe()

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path=settings.CHROME_PATH)
    l = LoginPage(driver,settings.URL)
    l.login("jiangliulin@163.com","baimaonv08340822")