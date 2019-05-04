from page.register_page import RegisterPage

class RegisterBusiness:
    def __init__(self,driver):
        self.driver = driver
        self.register_p = RegisterPage(self.driver)

    # def register(self,*args,**kwargs):
    #     self.register_p.get_username_element().