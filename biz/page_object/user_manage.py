#coding:utf-8
from biz.common.web_common import WebCommon
from selenium.webdriver.common.by import By
from biz.common.get_logger import get_logger
import time
from biz.common.read_data import get_yaml_data,yamlstr_to_tuple,con_mysql
from biz.get_path import *

logger = get_logger()
data = get_yaml_data(element_data)


"""用户管理主要功能：用户查询，添加，冻结、解冻"""
#用户查询 姓名
username_element = yamlstr_to_tuple(data["username_element"])
#账号
user_account_element = yamlstr_to_tuple(data["user_account_element"])
#账号状态
user_account_status_frame_element = yamlstr_to_tuple(data["user_account_status_frame_element"])
user_account_status_element = yamlstr_to_tuple(data["user_account_status_element"])
#查询
user_search_element = yamlstr_to_tuple(data["user_search_element"])
#添加
user_add_element = yamlstr_to_tuple(data["user_add_element"])
user_freeze_element = yamlstr_to_tuple(data["user_freeze_element"])
user_unfreeze_element = yamlstr_to_tuple(data["user_unfreeze_element"])
#选择框
checkbox_element = yamlstr_to_tuple(data["checkbox_element"])

#添加的账号、姓名、系统、角色
add_user_account_element = yamlstr_to_tuple(data["add_user_account_element"])
add_user_name_element = yamlstr_to_tuple(data["add_user_name_element"])
add_sys_frame_element = yamlstr_to_tuple(data["add_sys_frame_element"])

add_role_frame_element = yamlstr_to_tuple(data["add_role_frame_element"])

#点击+号
add_user_plus_element = yamlstr_to_tuple(data["add_user_plus_element"])
#确认按钮
confirm_element = yamlstr_to_tuple(data["confirm_element"])
#重置密码
user_reset_password_element = yamlstr_to_tuple(data["user_reset_password_element"])
#查询
# username = '小白'
# useraccount = "test003"
#添加
# add_useraccount = "luwenying897"
# add_username = "奶奶"


class UserManage(WebCommon):
    _params = {}

    def user_search(self,username,useraccount):
        self.input(username,username_element)
        self.input(useraccount,user_account_element)
        self.click(user_account_status_frame_element)
        self.execute_js_click(user_account_status_element)
        self.click(user_search_element)

    def user_add(self,add_useraccount,add_username,add_sys_name,add_role_name):
        self._params["add_sys_name"] = add_sys_name
        self._params["add_role_name"] = add_role_name
        account_select_sql = f"select * from merchant_user where account='{add_useraccount}' or user_name='{add_username}' ;"
        account_del_sql =  f"delete from merchant_user where account='{add_useraccount}' or user_name='{add_username}';"
        res = con_mysql("selectall",account_select_sql)
        print("查询结果为：",res)
        if res!=None:
            con_mysql("del",account_del_sql)

        new_data = self.replace_yaml_variable(data,self._params)
        add_sys_name_element = yamlstr_to_tuple(new_data["add_sys_name_element"])
        add_role_name_element = yamlstr_to_tuple(new_data["add_role_name_element"])

        self.click(user_add_element)
        self.input(add_useraccount,add_user_account_element)
        self.input(add_username,add_user_name_element)
        self.click(add_sys_frame_element)
        self.execute_js_click(add_sys_name_element)
        self.click(add_role_frame_element)
        self.execute_js_click(add_role_name_element)
        self.confirm()

    def user_modify(self):
        pass

    def user_freeze(self,username,useraccount):
        self.user_search(username,useraccount)
        self.click(checkbox_element)
        self.click(user_freeze_element)
        # self.click(confirm_element)
        self.confirm()

    def user_unfreeze(self,username,useraccount):
        self.user_search(username,useraccount)
        self.click(checkbox_element)
        self.click(user_unfreeze_element)
        # self.click(confirm_element)
        self.confirm()

    def reset_user_password(self,username,useraccount):
        self.user_search(username,useraccount)
        self.click(user_reset_password_element)
        self.confirm()


