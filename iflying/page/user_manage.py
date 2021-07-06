#coding:utf-8
from public_common.web_common import WebCommon
from public_common.read_data import get_yaml_data,yamlstr_to_tuple
from iflying.get_path import *

data = get_yaml_data(corp_manage_element)



class UserManage(WebCommon):

    def search_user(self,username=None):
        username_element = yamlstr_to_tuple(data["username_element"])
        search_btn_element = yamlstr_to_tuple(data["search_btn_element"])
        if username:
            self.wait_element_visible(username_element)
            self.clear_input(username,username_element)
        self.click(search_btn_element)


    def user_synchronize(self):
        user_synchronize_element = yamlstr_to_tuple(data["user_synchronize_element"])
        self.wait_element_visible(user_synchronize_element)
        self.click(user_synchronize_element)


    def set_user_permission(self,role_name):
        set_user_permissin_element = yamlstr_to_tuple(data["set_user_permissin_element"])
        set_user_role_frame_element = yamlstr_to_tuple(data["set_user_role_frame_element"])
        select_user_role_element = yamlstr_to_tuple(data["select_user_role_element"].replace("$role_name",role_name))
        confirm_element = yamlstr_to_tuple(data["confirm_element"])

        self.wait_element_visible(set_user_permissin_element)
        set_user_permissin_elements = self.locates(set_user_permissin_element)
        self.click(set_user_permissin_elements[1])
        self.wait_element_visible(set_user_role_frame_element)
        self.click(set_user_role_frame_element)
        self.execute_js_click(select_user_role_element)
        self.click(confirm_element)


