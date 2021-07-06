#coding:utf-8
from selenium.webdriver.common.by import By

from iflying.get_path import login_element
from iflying.page.corp_manage import CorpManage
from iflying.page.customer_manage import CustomerManage
from iflying.page.language_manage import LanguageManage
from public_common.web_common import WebCommon
from public_common.read_data import get_yaml_data,replace_variable,yamlstr_to_tuple

data = get_yaml_data(login_element)
customer_manager_element = yamlstr_to_tuple(data["menu"]["customer_manager_element"])
language_manage_element = yamlstr_to_tuple(data["menu"]["language_manage_element"])
corp_manage_element = yamlstr_to_tuple(data["menu"]["corp_manage_element"])

class Index(WebCommon):

    def customer_manager_index(self):
        """进入客户管理页面"""
        self.wait_element_visible(customer_manager_element)
        self.click(customer_manager_element)
        return CustomerManage(self._driver)

    def language_manage_index(self):
        """进入话术管理界面"""
        self.wait_element_visible(language_manage_element)
        self.click(language_manage_element)
        return LanguageManage(self._driver)

    def corp_manage_index(self):
        """进入企业管理界面"""
        self.wait_element_visible(corp_manage_element)
        self.click(corp_manage_element)
        return CorpManage(self._driver)



