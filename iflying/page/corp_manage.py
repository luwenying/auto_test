#coding:utf-8

from selenium.webdriver.common.by import By
from public_common.read_data import get_yaml_data,yamlstr_to_tuple
from iflying.page.permission_manage import PermissionManage
from iflying.page.user_manage import UserManage
from public_common.web_common import WebCommon
from iflying.get_path import *


data = get_yaml_data(corp_manage_element)
#用户管理菜单
user_manage_menu_element = yamlstr_to_tuple(data["user_manage_menu_element"])
#权限管理菜单
permission_manage_menu_element = yamlstr_to_tuple(data["permission_manage_menu_element"])


class CorpManage(WebCommon):

    def user_manage(self):
        """进入用户管理页面"""
        self.wait_element_visible(user_manage_menu_element)
        self.click(user_manage_menu_element)
        return UserManage(self._driver)


    def permission_manage(self):
        """进入权限管理页面"""
        self.wait_element_visible(permission_manage_menu_element)
        self.click(permission_manage_menu_element)
        return PermissionManage(self._driver)