#coding:utf-8
from iflying.page.login import Login
import pytest
from iflying.get_path import *
from public_common.read_data import yamlstr_to_tuple,get_yaml_data,con_mysql
from public_common.get_driver import get_driver
from time import sleep



class TestManage():
    def setup_class(self):
        self.driver = get_driver()
        self.login = Login(self.driver)
        self.data = get_yaml_data(all_data)
        print("-------------", self.data)
        self.language_manage = self.data["language_manage"]
        self.language = self.login.login(self.data["url"]).language_manage_index()
        self.language.into_language_manager()
        self.assert_add_scene = yamlstr_to_tuple(self.language_manage["assert_add_scene"])

    # @pytest.mark.parametrize("data", [get_yaml_data(all_data)])
    def test_add_scene(self):
        # print("-------------", data)
        self.language.add_scene(self.language_manage["add_scene_name"],self.language_manage["add_industry_name"],self.language_manage["add_descript"])
        try:
            self.language.wait_element_visible(self.assert_add_scene)
            txt = self.language.get_txt(self.assert_add_scene)
            assert txt == self.language_manage["add_scene_name"]
        except Exception as e:
            assert False

    def test_modify_scene(self):
        modify_scene_name = self.language_manage["modify_scene_name"]
        modify_descript = self.language_manage["modify_descript"]
        self.language.modify_scene(modify_scene_name,modify_descript)
        try:
            self.language.wait_element_visible(self.assert_add_scene)
            txt = self.language.get_txt(self.assert_add_scene)
            assert txt == self.language_manage["modify_scene_name"]
        except Exception as e:
            assert False

    def test_scene_enable_or_disable(self):
        disable_or_enble_scene_name = self.language_manage["disable_or_enble_scene_name"]
        assert_disable_or_enble_scene = self.language_manage["assert_disable_or_enble_scene"].replace("$scene_name",disable_or_enble_scene_name)
        before_scene_status = con_mysql("iflying","selectone",assert_disable_or_enble_scene)["category_status"]
        print(f"场景启用/禁用前的状态：{before_scene_status}")
        self.language.scene_enable_or_disable(disable_or_enble_scene_name)
        sleep(1)
        after_scene_status = con_mysql("iflying", "selectone", assert_disable_or_enble_scene)["category_status"]
        print(f"场景启用/禁用后的状态：{after_scene_status}")
        assert before_scene_status != after_scene_status

    def test_cancel_scene(self):
        modify_scene_name = self.language_manage["modify_scene_name"]
        assert_cancel_scene = self.language_manage["assert_cancel_scene"].replace("$scene_name",modify_scene_name)
        self.language.cancel_scene()
        cancel_res = con_mysql("iflying","selectall",assert_cancel_scene)
        assert cancel_res is None

    def test_add_language(self):
        add_question = self.language_manage["add_question"]
        add_intention = self.language_manage["add_intention"]
        add_answer = self.language_manage["add_answer"]
        add_start_date = self.language_manage["add_start_date"]
        add_end_date = self.language_manage["add_end_date"]
        add_start_time = self.language_manage["add_start_time"]
        add_end_time = self.language_manage["add_end_time"]
        assert_sql = self.language_manage["assert_sql"].replace("$add_question",add_question)
        # print(assert_sql)
        del_sql = self.language_manage["del_sql"].replace("$add_question",add_question)
        res = con_mysql("iflying","selectall",assert_sql)
        if res:
            con_mysql("iflying","del",del_sql)
        self.language.add_language(add_question,add_intention,add_answer,add_start_date,add_end_date,add_start_time,add_end_time)
        add_res = con_mysql("iflying","selectall",assert_sql)
        assert add_res is not None



    def test_modify_language(self):
        search_modify_question = self.language_manage["search_modify_question"]
        modify_question = self.language_manage["modify_question"]
        modify_intention = self.language_manage["modify_intention"]
        modify_answer = self.language_manage["modify_answer"]
        modify_start_date = self.language_manage["modify_start_date"]
        modify_end_date = self.language_manage["modify_end_date"]
        modify_start_time = self.language_manage["modify_start_time"]
        modify_end_time = self.language_manage["modify_end_time"]
        assert_sql = self.language_manage["assert_sql"].replace("$add_question", modify_question)
        del_sql = self.language_manage["del_sql"].replace("$add_question", modify_question)
        res = con_mysql("iflying", "selectall", assert_sql)
        if res:
            con_mysql("iflying", "del", del_sql)
        self.language.modify_language(modify_question,modify_intention,modify_answer,modify_start_date,modify_end_date,modify_start_time,modify_end_time,search_modify_question)
        modify_res = con_mysql("iflying", "selectall", assert_sql)
        assert modify_res is not None


    def test_language_disable(self):
        search_disable_question = self.language_manage["search_disable_question"]
        assert_sql = self.language_manage["assert_sql"].replace("$add_question", search_disable_question)
        before_content_status = con_mysql("iflying","selectone",assert_sql)["content_status"]
        print(f"话术禁用前的状态为：{before_content_status}")
        self.language.language_disable(search_disable_question)
        sleep(1)
        after_content_status = con_mysql("iflying","selectone",assert_sql)["content_status"]
        print(f"话术禁用后的状态为：{after_content_status}")
        assert after_content_status != before_content_status

    def test_language_enable(self):
        search_enable_question = self.language_manage["search_enable_question"]
        assert_sql = self.language_manage["assert_sql"].replace("$add_question", search_enable_question)
        before_content_status = con_mysql("iflying", "selectone", assert_sql)["content_status"]
        print(f"话术禁用前的状态为：{before_content_status}")
        self.language.language_enable(search_enable_question)
        sleep(1)
        after_content_status = con_mysql("iflying", "selectone", assert_sql)["content_status"]
        print(f"话术禁用后的状态为：{after_content_status}")
        assert after_content_status != before_content_status

    def test_cancel_language(self):
        search_cancel_question = self.language_manage["search_cancel_question"]
        self.language.cancel_language(search_cancel_question)
        sleep(1)
        assert_sql = self.language_manage["assert_sql"].replace("$add_question", search_cancel_question)
        res = con_mysql("iflying", "selectone", assert_sql)
        assert res is None

    def test_synchronize(self):
        self.language.synchronize()



