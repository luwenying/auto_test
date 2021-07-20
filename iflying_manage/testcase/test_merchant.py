#coding:utf-8
from iflying_manage.page.login_page import Login
from public_common.get_driver import get_driver
import pytest
from public_common.read_data import get_yaml_data,yamlstr_to_tuple,con_mysql,replace_variable
from iflying_manage.get_path import *
from public_common.get_logger import get_logger
import inspect

logger = get_logger()
data = get_yaml_data(all_data)
class TestMerchant():
    logger.info("开始商户管理测试！")
    def setup(self):
        driver = get_driver()
        self.login = Login(driver)
        self.merchant = self.login.login(data["login"]["username"], data["login"]["password"], data["login"]["sysname"]).left_menu_click(data["merchant"]["first_menu"],data["merchant"]["second_menu"])
        self.merchant_data = data["merchant"]

    def teardown(self):
        # self.merchant.sleep(2)
        self.merchant.close()

    # @pytest.mark.skip
    def test_search_merchant(self):
        logger.info(f"开始商户管理:{inspect.stack()[0][3]}测试")
        test_search_merchant_data = self.merchant_data["search_merchant"]
        merchant_name = test_search_merchant_data["merchant_name"]
        merchant_status = test_search_merchant_data["merchant_status"]
        start_date = test_search_merchant_data["start_date"]
        end_date = test_search_merchant_data["end_date"]
        start_time = test_search_merchant_data["start_time"]
        end_time = test_search_merchant_data["end_time"]
        assert_element = yamlstr_to_tuple(test_search_merchant_data["assert_element"])
        self.merchant.search_merchant(merchant_name,merchant_status,start_date,end_date,start_time,end_time)
        self.merchant.wait_element_visible(assert_element)
        txt = self.merchant.get_txt(assert_element)
        assert merchant_name in txt


    def test_allocate_industry(self):
        logger.info(f"开始商户管理:{inspect.stack()[0][3]}测试")
        test_allocate_industry_data = self.merchant_data["test_allocate_industry"]
        merchant_name = test_allocate_industry_data["merchant_name"]
        industrys = yamlstr_to_tuple(test_allocate_industry_data["industry"])
        self.merchant.allocate_industry(merchant_name,industrys)
        allocate_industry = self.merchant.get_industry_detail()
        # assert_industry = []
        for industry in industrys:
            key_v = industry["first_industry"]
            value_v = industry["second_industry"]
            for value in value_v:
                assert_data = key_v + "-" + value
                # assert_industry.append(assert_data)
                if assert_data not in allocate_industry:
                    print(f"{assert_data}没有配置成功")
                    assert False
                else:
                    assert True


if __name__=="__main__":
    data = get_yaml_data(all_data)
    industry = yamlstr_to_tuple(all_data["merchant"]["test_allocate_industry"]["industry"])
    print(industry)