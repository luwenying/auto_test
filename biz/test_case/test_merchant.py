#coding:utf-8
from selenium.webdriver.common.by import By

from biz.conftest import MyFixture
from public_common.get_driver import get_driver
from biz.page_object.merchant_page import MerchantManage
from biz.page_object.login_page import Login
from biz.common.get_logger import get_logger
import pytest
import yaml
from biz.get_path import *
from biz.common.read_data import con_mysql

class TestMerchant():

    def setup(self):
        self.driver = get_driver()
        self.login = Login(self.driver)
        self.logger = get_logger()
        self.merchantmanage = MerchantManage(self.driver)

    def teardown(self):
        self.login.close()


    # @pytest.mark.skip("不执行")
    @pytest.mark.parametrize("data",yaml.load(open(data_path+"add_merchant.yaml",encoding="utf-8"),Loader=yaml.FullLoader))
    def test_add_merchant(self,data):
        """添加商户"""
        self.login.login(data["name"], data["pwd"], data["sys"],)
        self.login.left_menu_click(data["menu"],data["second_menu"])
        self.merchantmanage.create_merchant(data["merchant_name"],data["username"],data["corp"],data["re_name"],data["telephone"])
        merchant_name = data["merchant_name"]
        select_sql = f"select * from merchant.merchant_base_info where merchant_name='{merchant_name}'"
        res = con_mysql("selectall",select_sql)
        assert res!=None


        #断言
        # try:
        #     assert_element = (By.XPATH,"//*[contains(text(),'首页')]")
        #     self.login.locate(assert_element)
        #     self.logger.info("进入系统成功")
        #     assert 1==1
        #
        # except Exception:
        #     self.logger.error("进入系统失败")
        #     assert 1==2

    # @pytest.mark.skip("不执行")
    @pytest.mark.parametrize("data",
                             yaml.load(open(data_path + "add_merchant.yaml", encoding="utf-8"), Loader=yaml.FullLoader))
    def test_modify_merchant(self,data):
        """添加商户信息"""
        self.login.login(data["name"], data["pwd"], data["sys"], )
        self.login.left_menu_click(data["menu"], data["second_menu"])
        self.merchantmanage.modify_merchant(data["modify_merchant_name"],data["modify_corp"],data["modify_re_name"],data["modify_telephone"])
        merchant_name = data["modify_merchant_name"]
        select_sql = f"select * from merchant.merchant_base_info where merchant_name='{merchant_name}'"
        res = con_mysql("selectall", select_sql)
        assert res != None







