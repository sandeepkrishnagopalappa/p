from pytestpackage.seleniumwrappers import Selenium_Wrappers


class Base_Page(Selenium_Wrappers):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_home_link(self):
        print('Click on Home Link Button')
