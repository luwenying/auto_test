#coding:utf-8
from string import Template

from selenium.webdriver.common.by import By

from iflying.get_path import *
from public_common.web_common import WebCommon
from public_common.read_data import get_yaml_data,replace_variable,yamlstr_to_tuple

data = get_yaml_data(customer_manage_element)
#二级菜单
customer_manager_element_second = yamlstr_to_tuple(data["customer_manager_element_second"])


class CustomerManage(WebCommon):

    def into_customer_manager(self):
        self.wait_element_visible(customer_manager_element_second)
        self.click(customer_manager_element_second)
        return True

    def search_customer(self,customer_name=None,customer_service=None,sex=None,start_time=None,end_time=None):
        new_data = replace_variable(data,customer_service=customer_service,sex=sex)
        # 客户搜搜
        # 客户名称
        customer_name_element = yamlstr_to_tuple(new_data["customer_name_element"])
        # 所属客服
        customer_service_element = yamlstr_to_tuple(new_data["customer_service_element"])
        customer_service_select_element = yamlstr_to_tuple(new_data["customer_service_select_element"])
        # 性别
        customer_sex_element = yamlstr_to_tuple(new_data["customer_sex_element"])
        customer_sex_select_element = yamlstr_to_tuple(new_data["customer_sex_select_element"])
        # 时间控件
        start_time_element = yamlstr_to_tuple(new_data["start_time_element"])
        end_time_element = yamlstr_to_tuple(new_data["end_time_element"])
        confirm_element = yamlstr_to_tuple(new_data["confirm_element"])
        # 查询
        search_btn_element = yamlstr_to_tuple(new_data["search_btn_element"])

        if customer_name:
            self.wait_element_visible(customer_name_element)
            self.input(customer_name,customer_name_element)
        if customer_service:
            self.click(customer_service_element)
            self.wait_element_visible(customer_service_select_element)
            self.click(customer_service_select_element)
        if sex:

            self.click(customer_sex_element)
            self.wait_element_visible(customer_sex_select_element)
            self.click(customer_sex_select_element)

        if start_time and end_time:
            self.wait_element_visible(start_time_element)
            self.click(start_time_element)
            input_start_time_element = self.locates(start_time_element)
            input_end_time_element = self.locates(end_time_element)
            self.input(start_time,input_start_time_element[1])
            self.clear_input(end_time,input_end_time_element[1])
            self.click(confirm_element)

        self.wait_element_visible(search_btn_element)
        self.click(search_btn_element)
        return True

    def update_customer(self):
        # 更新数据
        update_btn_element = yamlstr_to_tuple(data["update_btn_element"])
        self.wait_element_visible(update_btn_element)
        self.click(update_btn_element)
        return True






if __name__=="__main__":
    pass

