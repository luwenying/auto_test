#condig:utf-8
from public_common.web_common import WebCommon
from public_common.read_data import get_yaml_data,yamlstr_to_tuple
from iflying_manage.get_path import *


data = get_yaml_data(domain_manage_element)
#时间控件定位元素
start_date_element = yamlstr_to_tuple(data["start_date_element"])
end_date_element = yamlstr_to_tuple(data["end_date_element"])
start_time_element = yamlstr_to_tuple(data["start_time_element"])
end_time_element = yamlstr_to_tuple(data["end_time_element"])
confirm_element = yamlstr_to_tuple(data["confirm_element"])
#禁用、启用、同步确定按钮
enable_confirm_element = yamlstr_to_tuple(data["enable_confirm_element"])


class DomainManage(WebCommon):

    def search_domain(self, domain):
        search_domain_element = yamlstr_to_tuple(data["search_domain_element"])
        self.wait_input(domain,search_domain_element)

    def input_time(self,start_date,end_date,start_time=None,end_time=None):
        if start_date and end_date:
            self.wait_element_visible(start_date_element)
            self.click(start_date_element)
            # 输入日期年月日
            input_start_date_elements = self.locates(start_date_element)
            input_end_date_elements = self.locates(end_date_element)
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

    def search_intention(self,intention=None,status=None,start_date=None,end_date=None,start_time=None,end_time=None):
        search_btn_element = yamlstr_to_tuple(data["search_btn_element"])
        if intention:
            search_intention_element = yamlstr_to_tuple(data["search_intention_element"])
            self.wait_input(intention,search_intention_element)
        if status:
            search_status_frame_element = yamlstr_to_tuple(data["search_status_frame_element"])
            search_status_element =yamlstr_to_tuple(data["search_status_element"].replace("$status",status))
            self.wait_click(search_status_frame_element)
            self.execute_js_click(search_status_element)
        if start_date and end_date:
            self.input_time(start_date,end_date,start_time,end_time)
        self.wait_click(search_btn_element)


    def modify_intention(self,intention,question,answer):
        modify_element = yamlstr_to_tuple(data["modify_element"])
        modify_question_element = yamlstr_to_tuple(data["modify_question_element"])
        modify_answer_element = yamlstr_to_tuple(data["modify_answer_element"])
        modify_confirm_element = yamlstr_to_tuple(data["modify_confirm_element"])
        self.search_intention(intention)
        self.wait_click(modify_element)
        self.wait_element_visible(modify_question_element)
        self.clear_input(question,modify_question_element)
        self.clear_input(answer,modify_answer_element)
        self.click(modify_confirm_element)


    def enable_or_disable(self,intention):
        enable_or_disable_element = yamlstr_to_tuple(data["enable_or_disable_element"])

        self.search_intention(intention)
        self.wait_click(enable_or_disable_element)
        self.wait_click(enable_confirm_element)

    def synchronize_domain(self,first_domain,second_domain=None):
        first_domain_element = yamlstr_to_tuple(data["domain_element"].replace("$domain",first_domain))
        synchronize_domain = yamlstr_to_tuple(data["synchronize_domain"])
        self.wait_element_visible(first_domain_element)
        self.execute_js_click(first_domain_element)
        if second_domain:
            second_domain_element = yamlstr_to_tuple(data["domain_element"].replace("$domain", second_domain))
            self.wait_element_visible(second_domain_element)
            self.execute_js_click(second_domain_element)
        self.wait_click(synchronize_domain)
        self.wait_click(enable_confirm_element)
        self.search_intention()





