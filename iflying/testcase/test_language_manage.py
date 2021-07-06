#coding:utf-8
from iflying.page.login import Login
import pytest
from iflying.get_path import *
from public_common.read_data import yamlstr_to_tuple,get_yaml_data
from public_common.get_driver import get_driver




class TestManage():
    def setup_class(self):
        self.driver = get_driver()
        self.login = Login(self.driver)
        self.data = get_yaml_data(all_data)
        print("-------------", self.data)
        self.language_manage = self.data["language_manage"]
        self.language = self.login.login(self.data["url"]).language_manage_index()
        self.language.into_language_manager()

    # @pytest.mark.parametrize("data", [get_yaml_data(all_data)])
    def test_add_scene(self):
        # print("-------------", data)
        self.language.add_scene(self.language_manage["add_scene_name"],self.language_manage["add_industry_name"],self.language_manage["add_descript"])

    def test_modify_scene(self):
        modify_scene_name = self.language_manage["modify_scene_name"]
        modify_descript = self.language_manage["modify_descript"]
        self.language.modify_scene(modify_scene_name,modify_descript)

    def test_scene_enable_or_disable(self):
        self.language.scene_enable_or_disable()

    def test_cancel_scene(self):
        self.language.cancel_scene()

    def test_add_language(self):
        add_question = self.language_manage["add_question"]
        add_intention = self.language_manage["add_intention"]
        add_answer = self.language_manage["add_answer"]
        add_start_time = self.language_manage["add_start_time"]
        add_end_time = self.language_manage["add_end_time"]
        self.language.add_language(add_question,add_intention,add_answer,add_start_time,add_end_time)

    def test_modify_language(self):
        search_modify_question = self.language_manage["search_modify_question"]
        modify_question = self.language_manage["modify_question"]
        modify_intention = self.language_manage["modify_intention"]
        modify_answer = self.language_manage["modify_answer"]
        modify_start_time = self.language_manage["modify_start_time"]
        modify_end_time = self.language_manage["modify_end_time"]
        self.language.modify_language(modify_question,modify_intention,modify_answer,modify_start_time,modify_end_time,search_modify_question)


    def test_language_disable(self):
        search_disable_question = self.language_manage["search_disable_question"]
        self.language.language_disable(search_disable_question)

    def test_language_enable(self):
        search_enable_question = self.language_manage["search_enable_question"]
        self.language.language_enable(search_enable_question)


    def test_cancel_language(self):
        search_cancel_question = self.language_manage["search_cancel_question"]
        self.language.cancel_language(search_cancel_question)

    def test_synchronize(self):
        self.language.synchronize()



