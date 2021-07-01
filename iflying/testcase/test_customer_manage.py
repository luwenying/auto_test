#coding:utf-8
from iflying.page.index import Index
from iflying.page.login import Login
import pytest
from iflying.get_path import *
from public_common.read_data import yamlstr_to_tuple,get_yaml_data
from public_common.get_driver import get_driver


class TestCustomer():
    def setup(self):
        self.driver = get_driver()
        self.login = Login(self.driver)
    @pytest.mark.parametrize("data",[get_yaml_data(login_data)])
    def test_customer_manage(self,data):
        print("-------------",data)
        self.login.login(data["url"]).customer_manager_index()


