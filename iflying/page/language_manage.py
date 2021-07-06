#coding:utf-8
from selenium.webdriver.common.by import By

from iflying.get_path import language_manage_element
from public_common.read_data import get_yaml_data,yamlstr_to_tuple,replace_variable
from public_common.web_common import WebCommon



data = get_yaml_data(language_manage_element)

#二级菜单
language_manage_element_second = yamlstr_to_tuple(data["language_manage_element_second"])

class LanguageManage(WebCommon):
    #场景新增和编辑元素
    add_scene_element = yamlstr_to_tuple(data["add_scene_element"])
    add_scene_name_element = yamlstr_to_tuple(data["add_scene_name_element"])
    add_industry_name_element = yamlstr_to_tuple(data["add_industry_name_element"])
    add_descript_element = yamlstr_to_tuple(data["add_descript_element"])
    confirm_element = yamlstr_to_tuple(data["confirm_element"])
    #话术删除确定和启用和禁用确定元素
    cancel_confirm_element = yamlstr_to_tuple(data["cancel_confirm_element"])

    def into_language_manager(self):
        self.wait_element_visible(language_manage_element_second)
        self.click(language_manage_element_second)
        return True

    def add_scene(self,add_scene_name,add_industry_name,add_descript=None):

        # new_data = replace_variable(data,add_industry_name=add_industry_name)
        # 新增话术
        add_industry_name_select_element = yamlstr_to_tuple(data["add_industry_name_select_element"].replace("$add_industry_name",add_industry_name))
        self.wait_element_visible(self.add_scene_element)
        self.click(self.add_scene_element)
        #输入场景名称
        self.wait_element_visible(self.add_scene_name_element)
        self.input(add_scene_name,self.add_scene_name_element)
        #选择行业
        self.click(self.add_industry_name_element)
        self.wait_element_visible(add_industry_name_select_element)
        self.click(add_industry_name_select_element)
        #输入描述
        if add_descript:
            self.input(add_descript,self.add_descript_element)
        self.click(self.confirm_element)
        self.sleep(2)

    def modify_scene(self,modify_scene_name,modify_descript=None):
        modify_element = yamlstr_to_tuple(data["modify_element"])
        self.wait_element_visible(modify_element)
        self.click(modify_element)
        self.wait_element_visible(self.add_scene_name_element)
        self.clear_input(modify_scene_name,self.add_scene_name_element)
        if modify_descript:
            self.clear_input(modify_descript,self.add_descript_element)
        self.click(self.confirm_element)


    def scene_enable_or_disable(self):

        scene_enable_or_disable_element = yamlstr_to_tuple(data["scene_enable_or_disable_element"])
        self.wait_element_visible(scene_enable_or_disable_element)
        self.click(scene_enable_or_disable_element)


    def cancel_scene(self):
        self.into_more()
        del_scene_element = yamlstr_to_tuple(data["del_scene_element"])
        self.wait_element_visible(del_scene_element)
        self.click(del_scene_element)
        self.wait_element_visible(self.confirm_element,15)
        self.click(self.confirm_element)

    def into_more(self):
        self.more_element = yamlstr_to_tuple(data["more_element"])
        self.wait_element_visible(self.more_element)
        self.hover(self.more_element)

    def into_language(self):
        self.into_more()
        into_language_element = yamlstr_to_tuple(data["into_language_element"])
        self.wait_element_visible(into_language_element,20)
        self.click(into_language_element)

    def input_time(self,start_time,end_time):
        self.sleep(1)
        self.add_start_time_element = yamlstr_to_tuple(data["add_start_time_element"])
        self.add_end_time_element = yamlstr_to_tuple(data["add_end_time_element"])
        self.click(self.add_start_time_element)
        add_start_time_elements = self.locates(self.add_start_time_element)
        add_end_time_elements = self.locates(self.add_end_time_element)
        self.clear_input(start_time,add_start_time_elements[1])
        self.clear_input(end_time,add_end_time_elements[1])
        self.click(self.confirm_element)

    def add_modify_common(self,add_question,add_intention,add_answer,add_start_time=None,add_end_time=None):
        self.add_question_element = yamlstr_to_tuple(data["add_question_element"])
        self.add_intention_frame_element = yamlstr_to_tuple(data["add_intention_frame_element"])
        self.add_answer_element = yamlstr_to_tuple(data["add_answer_element"])
        self.add_intention_element = yamlstr_to_tuple(data["add_intention_element"].replace("$add_intention",add_intention))


        # 输入标准问
        self.wait_element_visible(self.add_question_element)
        self.clear_input(add_question, self.add_question_element)
        # 选择意图
        self.click(self.add_intention_frame_element)
        self.wait_element_visible(self.add_intention_element)
        self.execute_js_click(self.add_intention_element)
        #输入推荐答案
        self.clear_input(add_answer,self.add_answer_element)
        # 输入有效期
        if add_start_time and add_end_time:
            self.input_time(add_start_time, add_end_time)
        self.click(self.confirm_element)



    def add_language(self,add_question,add_intention,add_answer,add_start_time=None,add_end_time=None):
        self.into_language()
        add_language_btn_element = yamlstr_to_tuple(data["add_language_btn_element"])
        self.wait_element_visible(add_language_btn_element)
        self.click(add_language_btn_element)
        self.add_modify_common(add_question,add_intention,add_answer,add_start_time,add_end_time)



    def search_language(self,search_question=None,search_status=None,search_source=None):
        search_question_element = yamlstr_to_tuple(data["search_question_element"])
        search_status_frame_element = yamlstr_to_tuple(data["search_status_frame_element"])
        search_source_frame_element = yamlstr_to_tuple(data["search_source_frame_element"])
        search_btn_element = yamlstr_to_tuple(data["search_btn_element"])


        if search_question:

            self.clear_input(search_question,search_question_element)
        if search_status:
            search_status_element = yamlstr_to_tuple(data["search_status_element"].replace("$status", search_status))
            self.click(search_status_frame_element)
            self.click(search_status_element)
        if search_source:
            search_source_element = yamlstr_to_tuple(data["search_source_element"].replace("$source", search_source))
            self.click(search_source_frame_element)
            self.click(search_source_element)
        self.click(search_btn_element)
        # self.sleep(2)


    def modify_language(self,modify_question,modify_intention,add_answer,modify_start_time=None,modify_end_time=None,search_question=None):
        modify_language_btn_element = yamlstr_to_tuple(data["modify_language_btn_element"])
        if search_question:
            self.search_language(search_question)
        self.wait_element_visible(modify_language_btn_element)
        self.click(modify_language_btn_element)
        self.add_modify_common(modify_question,modify_intention,add_answer,modify_start_time,modify_end_time)


    def cancel_language(self,search_question=None):
        if search_question:
            self.search_language(search_question)
        cancel_language_element = yamlstr_to_tuple(data["cancel_language_element"])
        # self.cancel_confirm_element = yamlstr_to_tuple(data["cancel_confirm_element"])
        self.click(cancel_language_element)
        self.click(self.cancel_confirm_element)

    def language_enable(self,search_question=None):
        count = 0
        if search_question:
            self.search_language(search_question)
        try:
            enable_element = yamlstr_to_tuple(data["enable_element"])
            self.click(enable_element)
            self.click(self.cancel_confirm_element)
        except Exception as e:
            print(e.__str__())
            self.language_disable(search_question)
            self.language_enable(search_question)
            count +=1
            if count>=3:
                raise e



    def language_disable(self,search_question=None):
        count = 0
        if search_question:
            self.search_language(search_question)

        try:
            disable_element = yamlstr_to_tuple(data["disable_element"])
            self.click(disable_element)
            self.click(self.cancel_confirm_element)
        except Exception as e:
            print(e.__str__())
            self.language_enable(search_question)
            self.language_disable(search_question)
            count += 1
            if count >= 3:
                raise e

    def synchronize(self):
        """同步"""
        synchronize_element = yamlstr_to_tuple(data["synchronize_element"])
        synchronize_confirm_element = yamlstr_to_tuple(data["synchronize_confirm_element"])
        self.click(synchronize_element)
        self.wait_element_visible(synchronize_confirm_element)
        self.click(synchronize_confirm_element)




