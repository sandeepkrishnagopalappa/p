class Selenium_Wrappers:
    def __init__(self, driver):
        self.driver = driver

    def get_element_by_name(self, _name):
        return self.driver.find_element_by_name(_name)

    def get_element_by_id(self, _id):
        return self.driver.find_element_by_id(_id)

    def get_element_by_xpath(self, _xpath):
        return self.driver.find_element_by_xpath(_xpath)

    def get_title(self):
        return self.driver.getTitle()