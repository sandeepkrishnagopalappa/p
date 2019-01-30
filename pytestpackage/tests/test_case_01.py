import pytest
from pytestpackage.Pages.loginpage import Login_Page


@pytest.mark.usefixtures('before_suite')
class Test_validate_Login:
    def test_01(self):
        print('Running TC01!!!!!')
        lp = Login_Page(self.driver)
        lp.enter_user_name()
