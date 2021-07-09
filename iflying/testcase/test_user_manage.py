#coding:utf-8
from iflying.page.login import Login
from iflying.get_path import *
from public_common.read_data import yamlstr_to_tuple,get_yaml_data,con_mysql
from public_common.get_driver import get_driver

class TestUserManage():

    def setup_class(self):
        self.driver = get_driver()
        self.login = Login(self.driver)
        self.data = get_yaml_data(all_data)
        print("-------------", self.data)
        self.user_manage_data = self.data["corp_manage"]["user_manage"]
        self.user_manage = self.login.login(self.data["url"]).corp_manage_index().user_manage()

    def teardown_class(self):
        self.login.close()


    def test_search_user(self):
        username = self.user_manage_data["username"]
        self.user_manage.search_user(username)

    # def test_user_synchronize(self):
    #     self.user_manage.user_synchronize()

    def test_set_user_role(self):
        role_name = self.user_manage_data["role_name"]
        assert_user_role = yamlstr_to_tuple(self.user_manage_data["assert_user_role"])
        before_role = con_mysql("iflying","selectone",assert_user_role)
        self.user_manage.set_user_permission(role_name)




