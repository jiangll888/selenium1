from util.read_ini import ReadIni
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class GetElement:
    def __init__(self,driver,filename=None):
        self.driver = driver
        self.filename = filename
        self.r = ReadIni(self.filename)

    def get_element_key(self,key,section=None):
        element_key = self.r.get_value(key,section)
        if element_key:
            element_key_list = element_key.split(">")
        else:
            element_key_list = None
            print("配置文件中未取到该元素")
        return element_key_list

    def get_element(self,key,section=None):
        key_list = self.get_element_key(key,section)
        wait = WebDriverWait(self.driver,15)
        print("####################")
        print(key_list[1])
        try:
            if key_list[0] == 'id':
                key_tuple = (By.ID,key_list[1])
            elif key_list[0] == 'name':
                key_tuple = (By.NAME,key_list[1])
            else:
                key_tuple = (By.XPATH,key_list[1])
            element = wait.until(EC.visibility_of_element_located(key_tuple))
        except:
            print("元素未找到")
            element = None
        return element

if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path=r"E:\tools\selenium\chromedriver_win32\chromedriver.exe")
    driver.get("http://www.5itest.cn/register")
    time.sleep(2)
    g = GetElement(driver)
    print(g.get_element("username"))




