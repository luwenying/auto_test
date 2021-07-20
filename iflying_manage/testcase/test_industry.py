#coding:utf-8
from string import Template
from time import sleep

from iflying_manage.page.login_page import Login
from public_common.get_driver import get_driver
import pytest
from public_common.read_data import get_yaml_data,yamlstr_to_tuple,con_mysql,replace_variable
from iflying_manage.get_path import *
from public_common.get_logger import get_logger
import inspect


logger = get_logger()
data = get_yaml_data(all_data)
login_data = data["login"]
industry_data = data["industry"]

class TestIndustry():
    logger.info("开始行业管理测试")
    def setup(self):
        driver = get_driver()
        self.login = Login(driver)
        self.industry = self.login.login(login_data["username"], login_data["password"], login_data["sysname"]).left_menu_click(industry_data["first_menu"],industry_data["second_menu"])

    def teardown(self):
        self.login.close()

    @pytest.mark.skip
    def test_search(self):
        """查询行业"""
        self.industry.search_industry(industry_data["test_search"]["industry_name"])


    def del_same_industry(self,assert_sql,del_sql):
        """删除具有相同行业名称"""
        res = con_mysql("merchant_center", "selectall", assert_sql)
        logger.info("判断是否有重命,查询的结果是：",res)
        if res:
            logger.info("存在同样的名称行业，先删除")
            con_mysql("merchant_center", "del", del_sql)
        sleep(1)

    def assert_industry(self,assert_sql,assert_str):
        """断言生成行业是否成功"""
        sleep(1)
        res = con_mysql("merchant_center", "selectall", assert_sql)
        logger.info(f"断言结果：{res}")
        if res:
            result = res[0]["deleted"]
            assert result == assert_str

    def assert_domain(self,domain):
        """判断领域是否已经被绑定了，被绑定则设置为空"""
        assert_domain_data = industry_data["assert_domain"]
        domain_sql = assert_domain_data["domain_sql"].replace("$domain",str(domain))
        id = str(con_mysql("km","selectall",domain_sql)[0]["id"])
        industry_domain_sql = assert_domain_data["industry_domain_sql"].replace("$id",id)
        res = con_mysql("merchant_center","selectall",industry_domain_sql)
        if res:
            update_industry_domain_sql = assert_domain_data["update_industry_domain_sql"].replace("$id",id)
            con_mysql("merchant_center","update",update_industry_domain_sql)


    # @pytest.mark.skip
    def test_add_first_industry(self):
        """新增第一级行业"""
        # logger.info(f"开始行业管理:{inspect.stack()[0][3]}测试")
        test_add_first_industry_data = industry_data["test_add_first_industry"]
        assert_sql = test_add_first_industry_data["assert_sql"].replace("$industry_name",test_add_first_industry_data["industry_name"])
        del_sql = test_add_first_industry_data["del_sql"].replace("$industry_name", test_add_first_industry_data["industry_name"])
        self.del_same_industry(assert_sql,del_sql)
        self.industry.add_first_industry(test_add_first_industry_data["industry_name"],test_add_first_industry_data["descript"])
        self.assert_industry(assert_sql,"normal")


    # @pytest.mark.skip
    def test_modify_first_industry(self):
        """修改第二级行业"""
        logger.info(f"开始行业管理:{inspect.stack()[0][3]}测试")
        test_modify_first_industry_data = industry_data["test_modify_first_industry"]
        before_industry_name = test_modify_first_industry_data["before_industry_name"]
        after_industry_name = test_modify_first_industry_data["after_industry_name"]
        descript = test_modify_first_industry_data["descript"]
        assert_sql = test_modify_first_industry_data["assert_sql"].replace("$industry_name", after_industry_name)
        del_sql = test_modify_first_industry_data["del_sql"].replace("$industry_name", after_industry_name)
        self.del_same_industry(assert_sql, del_sql)
        self.industry.modify_first_industry(before_industry_name,after_industry_name,descript)
        self.assert_industry(assert_sql,"normal")



    # @pytest.mark.skip
    def test_add_second_industry(self):
        """新增第一级行业"""
        logger.info(f"开始行业管理:{inspect.stack()[0][3]}测试")
        test_add_second_industry_data = industry_data["test_add_second_industry"]
        first_name = test_add_second_industry_data["first_name"]
        second_name = test_add_second_industry_data["second_name"]
        domain = test_add_second_industry_data["domain"]
        descript = test_add_second_industry_data["descript"]
        assert_sql = Template(test_add_second_industry_data["assert_sql"]).substitute(second_name=second_name,first_name=first_name)
        del_sql = Template(test_add_second_industry_data["del_sql"]).substitute(second_name=second_name)
        select_sql = Template(test_add_second_industry_data["select_sql"]).substitute(second_name=second_name)
        self.assert_domain(domain)
        self.del_same_industry(select_sql,del_sql)
        self.industry.add_second_industry(first_name,second_name,domain,descript)
        self.assert_industry(assert_sql,"normal")

    # @pytest.mark.skip
    def test_modify_second_industry(self):
        """修改第二级行业"""
        logger.info(f"开始行业管理:{inspect.stack()[0][3]}测试")
        test_modify_second_industry_data = industry_data["test_modify_second_industry"]
        first_name = test_modify_second_industry_data["first_name"]
        before_second_name = test_modify_second_industry_data["before_second_name"]
        after_second_name = test_modify_second_industry_data["after_second_name"]
        domain = test_modify_second_industry_data["domain"]
        descript = test_modify_second_industry_data["descript"]
        assert_sql = Template(test_modify_second_industry_data["assert_sql"]).substitute(second_name=after_second_name, first_name=first_name)
        del_sql = Template(test_modify_second_industry_data["del_sql"]).substitute(second_name=after_second_name)
        select_sql = Template(test_modify_second_industry_data["select_sql"]).substitute(second_name=after_second_name)
        self.del_same_industry(select_sql,del_sql)
        self.assert_domain(domain)
        self.industry.modify_second_industry(first_name,before_second_name,after_second_name,domain,descript)
        self.assert_industry(assert_sql,"normal")

    # @pytest.mark.skip
    def test_cancel_second_industry(self):
        """删除第二级行业"""
        logger.info(f"开始行业管理:{inspect.stack()[0][3]}测试")
        test_cancel_second_industry_data = industry_data["test_cancel_second_industry"]
        first_name = test_cancel_second_industry_data["first_name"]
        second_name = test_cancel_second_industry_data["second_name"]
        assert_sql = Template(test_cancel_second_industry_data["assert_sql"]).substitute(second_name=second_name,first_name=first_name)
        logger.info(f"断言sql:{assert_sql}")
        self.industry.cancel_second_industry(first_name,second_name)
        self.assert_industry(assert_sql, "deleted")
    # @pytest.mark.skip
    def test_cancel_first_industry(self):
        """删除第一级行业"""
        logger.info(f"开始行业管理:{inspect.stack()[0][3]}测试")
        test_cancel_first_industry_data = industry_data["test_cancel_first_industry"]
        first_name = test_cancel_first_industry_data["first_name"]
        assert_sql = Template(test_cancel_first_industry_data["assert_sql"]).substitute(first_name=first_name)
        logger.info(f"断言的sql:{assert_sql}")
        self.industry.cancel_first_industry(first_name)
        self.assert_industry(assert_sql, "deleted")






if __name__=="__main__":
    test_add_second_industry_data = industry_data["test_add_second_industry"]
    first_name = test_add_second_industry_data["first_name"]
    second_name = test_add_second_industry_data["second_name"]
    assert_sql = replace_variable(test_add_second_industry_data["assert_sql"], second_name=second_name,
                                  first_name=first_name)
    print(assert_sql)