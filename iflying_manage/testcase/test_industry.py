#coding:utf-8
from time import sleep

from iflying_manage.page.login_page import Login
from public_common.get_driver import get_driver
import pytest


class TestIndustry():
    def setup_class(self):
        driver = get_driver()
        self.login = Login(driver)
        self.industry = self.login.login("luwenying", "Aa123456.", "产飞助手").left_menu_click("系统管理","行业管理")
    @pytest.mark.skip
    def test_search(self):
        self.industry.search_industry("保险")

    @pytest.mark.skip
    def test_add_first_industry(self):
        self.industry.add_first_industry("测试0002")

    @pytest.mark.skip
    def test_modify_first_industry(self):
        sleep(1)
        self.industry.modify_first_industry("测试0002","测试0002-修改后","自动化测试修改")

    @pytest.mark.skip
    def test_add_second_industry(self):
        sleep(1)
        self.industry.add_second_industry("行业","添加第二级","领域2")

    @pytest.mark.skip
    def test_modify_second_industry(self):
        sleep(1)
        self.industry.modify_second_industry("车险","宝马车01","宝马车01-修改后","测试st")

    def test_cancel_second_industry(self):
        self.industry.cancel_second_industry("行业","添加第二级")

    def test_cancel_first_industry(self):
        sleep(1)
        self.industry.cancel_first_industry("行业")
