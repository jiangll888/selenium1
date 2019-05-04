from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self,driver,url=None):
        self.driver = driver
        self.url = url
        self.action = ActionChains(self.driver)

    def open(self):
        self.driver.get(self.url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def send_msg(self,element,message):
        try:
            element.clear()
            element.send_keys(message)
        except:
             print("元素输入失败")

    def click_element(self,element):
        try:
            element.click()
        except:
            print("元素点击不到")

    def save_pic(self):
        self.driver.save_screenshot()

    def switch_iframe(self,element=None):
        try:
            if element == None:
                self.driver.switch_to.default_content()
            else:
                #self.wait.until(EC.visibility_of(element))
                self.driver.switch_to.frame(element)
        except:
            print("切换iframe失败")

    def switch_alert(self):
        try:
            al = self.driver.switch_to.alert
            return al
        except:
             print("切换alert失败")

    def drag_and_drop_element(self,source,target):
        try:
            self.action.drag_and_drop(source,target).perform()
        except:
            print("拖拽失败")

    def move_to_target(self,element):
        try:
            self.action.move_to_element(element).perform()
        except:
            print("鼠标悬停失败")