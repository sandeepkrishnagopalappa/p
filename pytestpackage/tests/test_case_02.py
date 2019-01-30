import pytest


@pytest.mark.usefixtures('before_suite')
class Test_validate_logout:
    def test_02(self):
        print('Running TC02!!!!!')
