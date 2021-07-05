#coding:utf-8
from iflying.page.login import Login
import pytest
from iflying.get_path import *
from public_common.read_data import yamlstr_to_tuple,get_yaml_data
from public_common.get_driver import get_driver




class TestManage():
    def setup(self):
        self.driver = get_driver()
        self.login = Login(self.driver)

    @pytest.mark.parametrize("data", [get_yaml_data(all_data)])
    def test_add_scene(self,data):
        print("-------------", data)
        self.language = self.login.login(data["url"]).language_manage_index()
        self.language.into_language_manager()
        language_manage = data["language_manage"]
        self.language.add_scene(language_manage["add_scene_name"],language_manage["add_industry_name"],language_manage["add_descript"])

