import logging
import time

from iflying_manage.page.login_page import Login
from public_common.get_driver import get_driver
import pytest
from public_common.read_data import get_yaml_data,yamlstr_to_tuple,con_mysql,generate_screenshot_dirname
from iflying_manage.get_path import *
from public_common.get_logger import get_logger




logger = get_logger()
data = get_yaml_data(all_data)

class TestDomain():
    logger.info("开始管理端领域知识库测试")

    def setup(self):
        driver = get_driver()
        self.login = Login(driver)
        self.domain = self.login.login(data["login"]["username"], data["login"]["password"], data["login"]["sysname"]).left_menu_click(data["domain"]["first_menu"],data["domain"]["second_menu"])
        self.domain_data = data["domain"]
        self.dirname = generate_screenshot_dirname()

    def teardown(self):
        self.domain.close()

    # @pytest.mark.skip
    def test_search_domain(self):
        """查询领域"""
        logger.info("开始管理端领域知识库:test_search_domain")
        test_search_domain_data = self.domain_data["test_search_domain"]
        domain = test_search_domain_data["domain"]
        assert_element = yamlstr_to_tuple(test_search_domain_data["assert_element"].replace("$domain",domain))
        self.domain.search_domain(domain)
        try:
            assert_elements = self.domain.locates(assert_element)
            for assert_element in assert_elements:
                attr = self.domain.get_attr("class",assert_element)
                assert "is-hidden" not in attr
        except Exception as e:
            logger.error(e)
            img_path = self.dirname + "/test_search_domain"+time.strftime("%Y%m%d%H%M")+".png"
            self.domain.screenshot(img_path)
            self.domain.allure_attach(img_path)
            assert False

    #
    # @pytest.mark.skip
    def test_search_intention(self):
        """查询话术"""
        test_search_intention_data = self.domain_data["test_search_intention"]
        intention = test_search_intention_data["intention"]
        status = test_search_intention_data["status"]
        start_date = test_search_intention_data["start_date"]
        end_date = test_search_intention_data["end_date"]
        start_time = test_search_intention_data["start_time"]
        end_time = test_search_intention_data["end_time"]
        assert_element = yamlstr_to_tuple(test_search_intention_data["assert_element"])
        self.domain.search_intention(intention,status,start_date,end_date,start_time,end_time)
        try:
            self.domain.wait_element_visible(assert_element)
            time.sleep(1)
            txts = self.domain.get_txts(assert_element)
            for txt in txts:
                assert intention in txt
        except Exception as e:
            logger.error(e)
            img_path = self.dirname + "/test_search_intention"+time.strftime("%Y%m%d%H%M")+".png"
            logger.info(f"img_path:{img_path}")
            self.domain.screenshot(img_path)
            self.domain.allure_attach(img_path)
            assert False



    # @pytest.mark.skip
    def test_modify_intention(self):
        """修改话术"""
        test_modify_intention_data = self.domain_data["test_modify_intention"]
        intention = test_modify_intention_data["intention"]
        question = test_modify_intention_data["question"]
        answer = test_modify_intention_data["answer"]
        self.domain.modify_intention(intention,question,answer)
        try:
            question, answer = self.domain.get_intention_detail()
            assert question==question
        except Exception as e:
            logger.error(e)
            img_path = self.dirname + "/test_modify_intention"+time.strftime("%Y%m%d%H%M")+".png"
            self.domain.screenshot(img_path)
            self.domain.allure_attach(img_path)
            assert False

    # @pytest.mark.skip
    def test_enable_or_disable(self):
        """禁用或启用话术"""
        test_enable_or_disable_data = self.domain_data["test_enable_or_disable"]
        intention = test_enable_or_disable_data["intention"]
        assert_element = yamlstr_to_tuple(test_enable_or_disable_data["assert_element"])
        before_txt = self.domain.get_txt(assert_element)
        logger.info(f"启用/禁用前：{before_txt}")
        self.domain.enable_or_disable(intention)
        time.sleep(1)
        try:
            after_txt = self.domain.get_txt(assert_element)
            logger.info(f"启用/禁用前：{after_txt}")
            # time.sleep(3)
            assert before_txt != after_txt
        except Exception as e:
            logger.error(e)
            img_path = self.dirname + "/test_enable_or_disable"+time.strftime("%Y%m%d%H%M")+".png"
            self.domain.screenshot(img_path)
            self.domain.allure_attach(img_path)
            assert False


    # @pytest.mark.skip
    def test_synchronize_domain(self):
        """同步话术"""
        self.domain.synchronize_domain("标准领域","公共类")
        assert True