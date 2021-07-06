#coding:utf-8
from iflying.page.login import Login
from iflying.get_path import *
from public_common.read_data import yamlstr_to_tuple,get_yaml_data
from public_common.get_driver import get_driver



class TestPermissionManage():

    def setup_class(self):
        self.driver = get_driver()
        self.login = Login(self.driver)
        self.data = get_yaml_data(all_data)
        print("-------------", self.data)
        self.permission_manage_data = self.data["corp_manage"]["permission_manage"]
        self.permission_manage = self.login.login(self.data["url"]).corp_manage_index().permission_manage()

    def teardown_class(self):
        self.login.close()

    def test_create_role(self):
        create_role_name = self.permission_manage_data["create_role_name"]
        create_role_data_scope = self.permission_manage_data["create_role_data_scope"]
        create_role_menu = yamlstr_to_tuple(self.permission_manage_data["create_role_menu"])
        create_role_descript = self.permission_manage_data["create_role_descript"]
        self.permission_manage.create_role(create_role_name,create_role_data_scope,create_role_menu,create_role_descript)

    def test_modify_role(self):
        modify_role_name = self.permission_manage_data["modify_role_name"]
        modify_role_data_scope = self.permission_manage_data["modify_role_data_scope"]
        modify_role_menu = yamlstr_to_tuple(self.permission_manage_data["modify_role_menu"])
        modify_role_descript = self.permission_manage_data["modify_role_descript"]
        modify_search_role_name = self.permission_manage_data["modify_search_role_name"]
        self.permission_manage.modify_role(modify_role_name,modify_role_data_scope,modify_role_menu,modify_role_descript,modify_search_role_name)



