#coding:utf-8

from public_common.web_common import WebCommon
from public_common.read_data import get_yaml_data,yamlstr_to_tuple
from iflying_manage.get_path import *

data = get_yaml_data(merchant_manage_element)
#时间控件定位元素
start_date_element = yamlstr_to_tuple(data["start_date_element"])
end_date_element = yamlstr_to_tuple(data["end_date_element"])
start_time_element = yamlstr_to_tuple(data["start_time_element"])
end_time_element = yamlstr_to_tuple(data["end_time_element"])
confirm_element = yamlstr_to_tuple(data["confirm_element"])



class MerchantManage(WebCommon):


    def input_time(self,start_date,end_date,start_time=None,end_time=None):
        if start_date and end_date:
            self.wait_element_visible(start_date_element)
            self.click(start_date_element)
            # 输入日期年月日
            input_start_date_elements = self.locates(start_date_element)
            input_end_date_elements = self.locates(end_date_element)
            self.sleep(1)
            self.clear_input(start_date,input_start_date_elements[1])
            self.clear_input(end_date,input_end_date_elements[1])
            if start_time == None:
                start_time = "00:00:00"
            else:
                start_time = start_time

            if end_time == None:
                end_time = "00:00:00"
            else:
                end_time = end_time
            # 输入时间
            self.clear_input(start_time, start_time_element)
            self.clear_input(end_time, end_time_element)
            self.click(confirm_element)

    def search_merchant(self,merchant_name=None,mechant_status=None,start_date=None,end_date=None,start_time=None,end_time=None):
        merchant_name_element = yamlstr_to_tuple(data["merchant_name_element"])
        merchant_status_frame_element = yamlstr_to_tuple(data["merchant_status_frame_element"])

        search_mechant_btn_element = yamlstr_to_tuple(data["search_mechant_btn_element"])
        if merchant_name:
            self.wait_input(merchant_name,merchant_name_element)
        if mechant_status:
            merchant_select_status_element = yamlstr_to_tuple(data["merchant_select_status_element"].replace("$status", mechant_status))
            self.wait_click(merchant_status_frame_element)
            self.wait_click(merchant_select_status_element)
        if start_date and end_date:
            self.input_time(start_date,end_date,start_time,end_time)
        self.wait_click(search_mechant_btn_element)


    def allocate_industry(self,merchant_name,industrys:list):
        allocate_industry_element = yamlstr_to_tuple(data["allocate_industry_element"])
        allocate_industry_frame_element = yamlstr_to_tuple(data["allocate_industry_frame_element"])
        allocate_confirm_element = yamlstr_to_tuple(data["allocate_confirm_element"])
        cancel_allocate_frame_element = yamlstr_to_tuple(data["cancel_allocate_frame_element"])

        self.search_merchant(merchant_name)
        self.wait_click(allocate_industry_element)
        self.wait_click(allocate_industry_frame_element)
        for industry in industrys:
            first_industry = industry["first_industry"]
            second_industrys = industry["second_industry"]
            select_first_industry_element = yamlstr_to_tuple(data["select_first_element"].replace("$industry_name",first_industry))
            self.wait_click(select_first_industry_element)
            for second_industry in second_industrys:
                select_second_industry_element = yamlstr_to_tuple(data["select_industry_element"].replace("$industry_name",second_industry))
                attr = self.get_attr("class",select_second_industry_element)
                if "is-checked" not in attr:
                    self.wait_click(select_second_industry_element)

        self.click(self.locates(cancel_allocate_frame_element)[-1])
        self.wait_click(allocate_confirm_element)









