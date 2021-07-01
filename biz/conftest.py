#coding:utf-8
import pytest

from biz.common.get_logger import get_logger
from biz.page_object.login_page import Login
from common.get_driver import get_driver



class MyFixture:
    @pytest.fixture(scope="class", autouse=True)
    def my_fixture(self):
        self.driver = get_driver()
        self.login = Login(self.driver)
        self.logger = get_logger()
        yield
        self.login.close()
