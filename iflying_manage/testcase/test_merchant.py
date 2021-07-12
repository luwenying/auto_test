#coding:utf-8
from iflying_manage.page.login_page import Login
from public_common.get_driver import get_driver
import pytest


class TestMerchant():
    def setup_class(self):
        driver = get_driver()
        self.login = Login(driver)
        self.merchant = self.login.login("luwenying", "Aa123456.", "产飞助手").left_menu_click("系统管理","商户管理")

    @pytest.mark.skip
    def test_search_merchant(self):
        self.merchant.search_merchant("火星公司","启用","2021-06-27","2021-06-29")

    def test_allocate_industry(self):
        self.merchant.allocate_industry("火星公司",[{"first_industry":"保险","second_industry":["人寿保险"]},{"first_industry":"银行01","second_industry":["平安银行"]}])