#coding:utf-8
import pytest
from public_common.get_driver import get_driver
from iflying.page.login import Login
from iflying.get_path import *
from public_common.read_data import get_yaml_data
import yaml

class TestLogin():
    data = get_yaml_data(login_data)

    def setup(self):
        self.driver = get_driver()
        self.login = Login(self.driver)

    def teardown(self):
        self.login.close()

    def test_login(self):
        print("登录的网址是：",self.data)
        self.login.login(self.data["url"])

if __name__=="__main__":
    data = yaml.load(open(login_data,encoding="utf-8"),Loader=yaml.FullLoader)
    print(data["url"])