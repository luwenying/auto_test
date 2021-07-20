#coding:utf-8
from public_common.web_common import WebCommon
from public_common.read_data import get_yaml_data,yamlstr_to_tuple
from iflying_manage.get_path import *
from iflying_manage.page.domain_manage import DomainManage
from iflying_manage.page.industry_manage import IndustryManage
from iflying_manage.page.merchant_manage import MerchantManage

data = get_yaml_data(main_menu_element)
# language_manage_element = yamlstr_to_tuple(data["language_manage_element"])
# domain_manage_element = yamlstr_to_tuple(data["domain_manage_element"])
# system_manage_element = yamlstr_to_tuple(data["system_manage_element"])
# merchant_manage_element = yamlstr_to_tuple(data["merchant_manage_element"])
# industry_manage_element = yamlstr_to_tuple(data["industry_manage_element"])



class MainMenu(WebCommon):


    def left_menu_click(self,main_menu,second_menu):
        """点击左侧大菜单"""
        main_menu_element = yamlstr_to_tuple(data["main_menu_element"].replace("$main_menu",main_menu))
        self.wait_click(main_menu_element)
        return self._left_second_menu_click(second_menu)

    def _left_second_menu_click(self, second_menu):
        """点击第二级菜单"""
        second_menu_element = yamlstr_to_tuple(data["second_menu_element"].replace("$second_menu", second_menu))
        # print(f"二级菜单为：{second_menu_element}")
        self.wait_click(second_menu_element)
        if second_menu == "领域知识库":
            return DomainManage(self._driver)
        elif second_menu == "商户管理":
            return MerchantManage(self._driver)
        elif second_menu == "行业管理":
            return IndustryManage(self._driver)