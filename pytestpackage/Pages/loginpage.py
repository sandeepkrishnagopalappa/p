from pytestpackage.Pages.basepage import Base_Page


class Login_Page(Base_Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_user_name(self):
        txt_user_name = self.get_element_by_name('firstname')
        txt_user_name.send_keys('Sandeep')

    def title(self):
        print(Base_Page.get_title(self))

