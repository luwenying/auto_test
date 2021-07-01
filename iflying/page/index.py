#coding:utf-8
from selenium.webdriver.common.by import By

from public_common.web_common import WebCommon


customer_manager_element = (By.XPATH,'//span[text()=“客户管理”]')

class Index(WebCommon):

    def customer_manager_index(self):
        self.click(customer_manager_element)