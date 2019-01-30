import pytest
from selenium import webdriver


@pytest.fixture(scope='class', params=['chrome'])
def before_suite(request):
    print('Running test on ', request.param)
    print('\n ********Launching Browser***********')
    if request.param.upper() == 'CHROME':
        driver = webdriver.Chrome(
            executable_path='C:\\Users\\ssuryaprasad\\Desktop\\Selenium Framework\\drivers\\chromedriver.exe')
    elif request.param.upper() == 'FIREFOX':
        print('Running test on ', request.param)
        driver = webdriver.Firefox(
            executable_path='C:\\Users\\ssuryaprasad\\Desktop\\Selenium Framework\\drivers\\geckodriver.exe')
    else:
        print('unknown Browser')
    driver.get('file:///C:/Users/ssuryaprasad/Desktop/Selenium%20Framework/HTML/testPage.html')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    print('*************Closing Browser***************')
    driver.quit()

