# coding:utf-8
import yaml

from biz.common.get_logger import get_logger
from biz.common.get_driver import get_driver
from biz.get_path import *
from biz.page_object.product_page import ProductManage
from biz.page_object.login_page import Login
import pytest


class TestProduct():

    def setup(self):
        self.driver = get_driver()
        self.login = Login(self.driver)
        self.product_manage = ProductManage(self.driver)
        self.logger = get_logger()

    def teardown(self):
        self.login.close()

    @pytest.mark.parametrize("data",
                             yaml.load(open(data_path + "product.yaml", encoding="utf-8"), Loader=yaml.FullLoader))
    def test_search_product(self,data):
        self.login.login(data["name"],data["pwd"],data["sys"])
        self.login.left_menu_click(data["menu"],data["second_menu"])
        self.product_manage.create_merchant_bind(data["bind_product_name"],data["bind_merchant_name"])
        self.product_manage.sleep(2)




