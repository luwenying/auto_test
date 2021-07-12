#coding:utf-8

from public_common.web_common import WebCommon
from public_common.read_data import get_yaml_data,yamlstr_to_tuple
from iflying_manage.get_path import *





data = get_yaml_data(industry_manage_element)

#共用
name_element = yamlstr_to_tuple(data["name_element"])
descript_element = yamlstr_to_tuple(data["descript_element"])
confirm_element = yamlstr_to_tuple(data["confirm_element"])
#编辑菜单
modify_element = yamlstr_to_tuple(data["modify_element"])
#删除菜单
cancel_element =  yamlstr_to_tuple(data["cancel_element"])
cancel_confirm_element = yamlstr_to_tuple(data["cancel_confirm_element"])



class IndustryManage(WebCommon):

    def search_industry(self,name):
        search_industry_element = yamlstr_to_tuple(data["search_industry_element"])
        self.wait_element_visible(search_industry_element)
        self.clear_input(name,search_industry_element)


    def add_and_modify_first_common(self,first_name,first_descript=None):
        self.wait_input(first_name, name_element)
        if first_descript:
            self.clear_input(first_descript, descript_element)
        self.click(confirm_element)

    def add_and_modify_second_common(self,second_name,domain=None,second_descript=None):
        relate_domain_element = yamlstr_to_tuple(data["relate_domain_element"])
        select_relate_domain_element = yamlstr_to_tuple(data["select_relate_domain_element"].replace("$add_domain",domain))
        self.wait_input(second_name,name_element)
        if domain:
            self.click(relate_domain_element)
            self.wait_element_visible(select_relate_domain_element)
            self.execute_js_click(select_relate_domain_element)
        if second_descript:
            self.wait_input(second_descript,descript_element)
        self.click(confirm_element)


    def add_first_industry(self,first_name,first_descript=None):
        add_first_element = yamlstr_to_tuple(data["add_first_element"])
        self.wait_click(add_first_element)
        self.add_and_modify_first_common(first_name,first_descript)


    def modify_first_industry(self,before_first_name,after_first_name,first_descript=None):
        select_first_element = yamlstr_to_tuple(data["select_first_element"].replace("$first_name", before_first_name))
        self.wait_click(select_first_element)
        self.wait_click(modify_element)
        self.add_and_modify_first_common(after_first_name,first_descript)


    def add_second_industry(self,first_name,second_name,domain,second_descript=None):
        select_first_element = yamlstr_to_tuple(data["select_first_element"].replace("$first_name",first_name))
        add_second_element = yamlstr_to_tuple(data["add_second_element"])
        self.wait_click(select_first_element)
        self.wait_click(add_second_element)
        self.add_and_modify_second_common(second_name,domain,second_descript)

    def modify_second_industry(self,first_name,before_second_name,after_second_name,domain=None,first_descript=None):
        select_first_element = yamlstr_to_tuple(data["select_first_element"].replace("$first_name", first_name))
        select_second_element = yamlstr_to_tuple(data["select_first_element"].replace("$first_name", before_second_name))
        self.wait_click(select_first_element)
        self.wait_click(select_second_element)
        self.wait_click(modify_element)
        self.add_and_modify_second_common(after_second_name,domain,first_descript)


    def cancel_second_industry(self,first_name,second_name):
        select_first_element = yamlstr_to_tuple(data["select_first_element"].replace("$first_name", first_name))
        select_second_element = yamlstr_to_tuple(data["select_first_element"].replace("$first_name", second_name))
        self.wait_click(select_first_element)
        self.wait_click(select_second_element)
        self.wait_click(cancel_element)
        self.wait_click(cancel_confirm_element)



    def cancel_first_industry(self,first_name):
        select_first_element = yamlstr_to_tuple(data["select_first_element"].replace("$first_name", first_name))
        self.wait_click(select_first_element)
        self.wait_click(cancel_element)
        self.wait_click(cancel_confirm_element)











