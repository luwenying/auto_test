#coding:utf-8
from biz.common.web_common import WebCommon
from selenium.webdriver.common.by import By
from biz.common.get_logger import get_logger
import time
from biz.common.read_data import get_yaml_data,yamlstr_to_tuple
from biz.get_path import *


logger = get_logger()
data = get_yaml_data(element_data)

#产品管理界面的元素
#查询元素 产品名称 商户名称 查询按钮 重置按钮
product_btn_element = yamlstr_to_tuple(data["product_btn_element"])
product_merchant_name_element =  yamlstr_to_tuple(data["product_merchant_name_element"])
product_search_element = yamlstr_to_tuple(data["product_search_element"])
#新建绑定
create_product_element = yamlstr_to_tuple(data["create_product_element"])
#停用
product_stop_element = yamlstr_to_tuple(data["product_stop_element"])


class ProductManage(WebCommon):
    _params = {}
    def product_search(self,product_name,merchant_name):
        self._params["product_name"] = product_name
        new_data = self.replace_yaml_variable(data,self._params)
        product_name_element = yamlstr_to_tuple(new_data["product_name_element"])
        self.click(product_btn_element)
        self.click(product_name_element)
        self.input(merchant_name,product_merchant_name_element)
        self.click(product_search_element)

    def create_merchant_bind(self,create_product_name,merchant_name):
        self._params["create_product_name"] = create_product_name
        self._params["merchant_name"] = merchant_name
        #点击新建绑定
        self.click(create_product_element)
        product_btn_ele = self.locates(product_btn_element)
        print("product_btn_element长度为%s"%len(product_btn_ele))
        #点击产品名称
        self.click(product_btn_ele[-2])
        #选择产品名称
        new_data = self.replace_yaml_variable(data,self._params)
        create_product_name_element =yamlstr_to_tuple(new_data["create_product_name_element"])
        product_name_ele = self.locates(create_product_name_element)
        print("product_name_element长度为%s" % len(product_name_ele))
        self.click(product_name_ele[-1])
        self.sleep(1)
        #点击商户名称
        self.click(product_btn_ele[-1])
        #选择商户名称
        new_merchant_name_element = yamlstr_to_tuple(new_data["new_merchant_name_element"])
        new_merchant_name_ele = self.locates(new_merchant_name_element)
        print("new_merchant_name_element长度为%s" % len(new_merchant_name_ele))
        self.execute_js_click(new_merchant_name_ele[-1])
        # self.click(new_merchant_name_ele[-1])
        self.confirm()


    def product_stop(self):
        self.click(product_stop_element)
        self.confirm()

