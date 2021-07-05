#coding:utf-8

from selenium.webdriver.common.by import By

from public_common.web_common import WebCommon

#二级菜单
language_manage_element_second = (By.XPATH,'//li[text()="话术管理"]')

class CorpManage(WebCommon):

    def into_customer_manager(self):
        self.click(language_manage_element_second)