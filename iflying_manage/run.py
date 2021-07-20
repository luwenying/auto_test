import pytest


if __name__=="__main__":
    #test_customer_manage
    #生成测试报告 allure generate . -o ../report/ --clean
    pytest.main(["-sv","testcase/test_industry.py::TestIndustry::test_add_first_industry.py","--alluredir=./result"])






