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
                                 start_date=customer_manage["start_date"],end_date=customer_manage["end_date"])
        # print(assert_data)
        # assert customer_manage["customer_name"] == assert_data
        assert_element = yamlstr_to_tuple(customer_manage["assert_customer_name"])
        try:
            self.customer.wait_element_visible(assert_element)
            txt = self.customer.get_txt(assert_element)
            print(txt)
            assert customer_manage["customer_name"]==txt
        except Exception as e:
            print(e)
            assert False

    # def test_update_customer(self):
    #     self.customer.update_customer()


