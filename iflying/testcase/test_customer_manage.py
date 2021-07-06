#coding:utf-8
from iflying.page.index import Index
from iflying.page.login import Login
import pytest
from iflying.get_path import *
from public_common.read_data import yamlstr_to_tuple,get_yaml_data
from public_common.get_driver import get_driver


class TestCustomer():
    def setup_class(self):
        self.driver = get_driver()
        self.login = Login(self.driver)

    @pytest.mark.parametrize("data",[get_yaml_data(all_data)])
    def test_customer_search(self,data):
        print("-------------",data)
        self.customer = self.login.login(data["url"]).customer_manager_index()
        self.customer.into_customer_manager()
        customer_manage = data["customer_manage"]
        self.customer.search_customer(customer_name=customer_manage["customer_name"],customer_service=customer_manage["customer_service"],sex=customer_manage["sex"],
                                 start_time=customer_manage["start_time"],end_time=customer_manage["end_time"])

    def test_update_customer(self):
        self.customer.update_customer()


