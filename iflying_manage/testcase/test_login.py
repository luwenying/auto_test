#coding:utf-8
from iflying_manage.page.login_page import Login
from public_common.get_driver import get_driver


class TestLogin():

    def setup(self):
        driver = get_driver()
        self.login = Login(driver)

    def test_login(self):
        self.login.login("luwenying", "Aa123456.", "产飞助手")