#coding:utf-8

# coding:utf-8
import yaml

from biz.common.get_logger import get_logger
from biz.common.get_driver import get_driver
from biz.common.read_data import con_mysql
from biz.get_path import *
from biz.page_object.user_manage import UserManage
from biz.page_object.login_page import Login
import pytest

class TestProduct():

    def setup(self):
        self.driver = get_driver()
        self.login = Login(self.driver)
        self.user_manage = UserManage(self.driver)
        self.logger = get_logger()

    def teardown(self):
        self.login.close()

    @pytest.mark.parametrize("data",
                             yaml.load(open(data_path + "user_manage.yaml", encoding="utf-8"),
                                       Loader=yaml.FullLoader))
    def test_user_add(self, data):
        self.login.login(data["name"], data["pwd"], data["sys"])
        self.login.left_menu_click(data["menu"], data["second_menu"])
        self.user_manage.user_add(data["add_account"],data["add_name"],data["add_sys_name"],data["add_role_name"])
        self.user_manage.sleep(2)
        add_useraccount = data["add_account"]
        add_username = data["add_name"]
        account_select_sql = f"select * from merchant_user where account='{add_useraccount}' or user_name='{add_username}' ;"
        res = con_mysql("select",account_select_sql)
        assert res!=None