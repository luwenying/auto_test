#coding:utf-8

from public_common.read_data import get_yaml_data,yamlstr_to_tuple
from iflying.get_path import *
from public_common.web_common import WebCommon

data = get_yaml_data(corp_manage_element)

class PermissionManage(WebCommon):


    def search_role(self,role=None):
        search_role_name_element = yamlstr_to_tuple(data["search_role_name_element"])
        search_role_btn_emelent = yamlstr_to_tuple(data["search_role_btn_emelent"])
        if role:
            self.wait_element_visible(search_role_name_element)
            self.clear_input(role,search_role_name_element)
        self.click(search_role_btn_emelent)


    def creat_and_modify_role_common(self,role_name,role_data_scope,role_menu:tuple,role_descript=None):
        role_name_element = yamlstr_to_tuple(data["role_name_element"])
        role_data_scope_element = yamlstr_to_tuple(data["role_data_scope_element"].replace("$role_data_scope",role_data_scope))
        role_descript_element = yamlstr_to_tuple(data["role_descript_element"])
        create_role_btn_element = yamlstr_to_tuple(data["create_role_btn_element"])

        self.wait_element_visible(role_name_element)
        self.clear_input(role_name,role_name_element)
        self.click(role_data_scope_element)
        if role_descript:
            self.clear_input(role_descript,role_descript_element)
            #没有选择的菜单
        all_menu = yamlstr_to_tuple(data["all_menu"])
        false_menu = []
        for menu in all_menu:
            if menu not in role_menu:
                false_menu.append(menu)
        print("没有选择的菜单为：",false_menu)
        #选择的菜单点√
        if isinstance(role_menu,tuple):
            for menu in role_menu:
                role_menu_element = yamlstr_to_tuple(data["role_menu_element"].replace("$role_menu",menu))
                attr = self.get_attr("class",role_menu_element)
                print("class属性值是：",attr)
                if "is-checked" not in attr:
                    self.click(role_menu_element)
        # else:
        #     role_menu_element = yamlstr_to_tuple(data["role_menu_element"].replace("$role_menu", role_menu))
        #     attr = self.get_attr("class", role_menu_element)
        #     print("class属性值是：", attr)
        #     if "is-checked" not in attr:
        #         self.click(role_menu_element)

                #不选择的菜单，取消选择
        for menu in false_menu:
            role_menu_element = yamlstr_to_tuple(data["role_menu_element"].replace("$role_menu", menu))
            attr = self.get_attr("class", role_menu_element)
            print("class属性值是：", attr)
            if "is-checked" in attr:
                self.click(role_menu_element)
        self.click(create_role_btn_element)


    def create_role(self,role_name,role_data_scope,role_menu:tuple,role_descript=None):
        creat_role_element = yamlstr_to_tuple(data["creat_role_element"])
        self.wait_element_visible(creat_role_element)
        self.click(creat_role_element)
        self.creat_and_modify_role_common(role_name,role_data_scope,role_menu,role_descript)

    def modify_role(self,role_name,role_data_scope,role_menu:tuple,role_descript=None,search_role_name=None):
        modify_role_element = yamlstr_to_tuple(data["creat_role_element"])
        if search_role_name:
            self.search_role(search_role_name)
        self.wait_element_visible(modify_role_element)
        self.click(modify_role_element)
        self.creat_and_modify_role_common(role_name,role_data_scope,role_menu,role_descript)









if __name__=="__main__":
    all_menu = ('首页', '客户管理', '客户标签', '话术管理', '用户管理', '权限管理')
    # all_menu = data["all_menu"]
    # new_all_menu = yamlstr_to_tuple(all_menu)
    # print(new_all_menu)
    # print(type(new_all_menu))
    role_menu = ("客户管理",'客户标签')
    false_menu = []
    for i in all_menu:
        if  i not in role_menu:
            false_menu.append(i)
    print(false_menu)
