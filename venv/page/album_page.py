from base.base_page import BasePage
from base.get_element import GetElement
from selenium import webdriver
from config import settings
from page.login_page import LoginPage
from page.home_page import HomePage
import time

class AlbumPage(BasePage):
    def __init__(self,driver):
        super(AlbumPage,self).__init__(driver)
        self.get_ele = GetElement(driver)

    def get_create_album_element(self):
        return self.get_ele.get_element("create_album_btn","album_element")

    def get_frame1_element(self):
        return self.get_ele.get_element("iframe1","album_element")

    def get_album_name_element(self):
        return self.get_ele.get_element("album_name","album_element")

    def get_confirm_btn_element(self):
        return self.get_ele.get_element("confirm_btn","album_element")

    def get_sort_btn_element(self):
        return self.get_ele.get_element("sort_btn","album_element")

    def get_self_def_btn_element(self):
        return self.get_ele.get_element("self_def_sort_btn","album_element")

    def get_album_A_element(self):
        return self.get_ele.get_element("album_A","album_element")

    def get_album_B_element(self):
        return self.get_ele.get_element("album_B","album_element")

    def get_album_C_element(self):
        return self.get_ele.get_element("album_C","album_element")

    def get_save_btn_element(self):
        return self.get_ele.get_element("save_btn","album_element")

    def get_album_test_element(self):
        return self.get_ele.get_element("album_test","album_element")

    def get_delete_btn_element(self):
        return self.get_ele.get_element("delete_btn","album_element")

    def get_del_confirm_element(self):
        return self.get_ele.get_element("del_confirm_btn","album_element")


    def create_album(self,album_name=None,album_desc=None,album_privilege=None):
        self.click_element(self.get_create_album_element())
        self.switch_iframe(self.get_frame1_element())
        if album_name:
            self.send_msg(self.get_album_name_element(),album_name)
        self.click_element(self.get_confirm_btn_element())
        #self.switch_iframe()

    def alert_accept(self,msg):
        alert = self.switch_alert()
        if alert.text == msg:
            return True
        else:
            return False
        alert.accept()

    def move(self):
        self.click_element(self.get_sort_btn_element())
        self.click_element(self.get_self_def_btn_element())
        self.drag_and_drop_element(al.get_album_A_element(),al.get_album_C_element())
        self.click_element(self.get_save_btn_element())

    def delete_album(self,album):
        self.move_to_target(album)
        self.click_element(self.get_delete_btn_element())
        self.click_element(self.get_del_confirm_element())

if __name__ == "__main__":
    driver = webdriver.Firefox(executable_path=settings.FIREFOX_PATH)
    l = LoginPage(driver, settings.URL)
    l.login("jiangliulin@163.com", "baimaonv08340822")
    h = HomePage(driver, settings.URL)
    h.enter_album()
    al = AlbumPage(driver)
    # al.create_album()
    # print(al.alert_accept("请输入相册名称！"))
    # al.move()
    # time.sleep(2)
    al.delete_album(al.get_album_test_element())