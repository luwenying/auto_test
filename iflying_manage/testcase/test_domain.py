from iflying_manage.page.login_page import Login
from public_common.get_driver import get_driver
import pytest


class TestDomain():
    def setup_class(self):
        driver = get_driver()
        self.login = Login(driver)
        self.domain = self.login.login("luwenying", "Aa123456.", "产飞助手").left_menu_click("话术管理","领域知识库")

    @pytest.mark.skip
    def test_search_domain(self):
        self.domain.search_domain("质疑类111")

    @pytest.mark.skip
    def test_search_intention(self):
        self.domain.search_intention("保险费","启用","2021-07-01","2021-07-13","08:05:05","23:05:05")

    @pytest.mark.skip
    def test_modify_intention(self):
        self.domain.modify_intention("保险费","保险费多少钱","根据年份而不同")

    @pytest.mark.skip
    def test_enable_or_disable(self):
        self.domain.enable_or_disable("保险费")

    def test_synchronize_domain(self):
        self.domain.synchronize_domain("标准领域","公共类")