import pytest
from selenium import webdriver
import time


def init_setup():
    global driver
    print('Running webdriver!!!!!!!')
    driver = webdriver.Chrome(executable_path="C:\\SeleniumWorkSpace\\SAFE\\Test_Library\\chromedriver.exe")
    driver.maximize_window()
    driver.get("file:///C:/Users/ssuryaprasad/Desktop/Selenium%20Framework/HTML/testPage.html")
    time.sleep(3)


def tear_down():
    print('Closing Browser')
    driver.quit()


@pytest.yield_fixture()
def setup():
    init_setup()
    yield
    tear_down()
