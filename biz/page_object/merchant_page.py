#coding:utf-8
from selenium.webdriver.common.by import By
from biz.common.web_common import WebCommon
from biz.common.read_data import get_yaml_data,yamlstr_to_tuple,con_mysql
from biz.get_path import *
from biz.common.get_logger import get_logger


logger = get_logger()
_data = get_yaml_data(element_data)

# print(_data)
#商户管理的元素：商户名称、查询、重置 新建商户 重置密码 编辑
#商户名称
merchant_name_element = yamlstr_to_tuple(_data["merchant_name_element"])
#查询按钮
search_btn_element = yamlstr_to_tuple(_data["search_btn_element"])
#重置按钮
reset_btn_element = yamlstr_to_tuple(_data["reset_btn_element"])
#重置密码
reset_password_element = yamlstr_to_tuple(_data["reset_password_element"])
#编辑
modify_element = yamlstr_to_tuple(_data["modify_element"])
#新建商户
create_merchant_element = yamlstr_to_tuple(_data["create_merchant_element"])
#创建商户需要填写的信息 商户名称、登录账号、公司全称、姓名、手机号码
create_merchant_msg_element = yamlstr_to_tuple(_data["create_merchant_msg_element"])
#确认按钮
confirm_element = yamlstr_to_tuple(_data["create_merchant_msg_element"])
#取消按钮
# concel_element = (By.XPATH,'//span[contains(text(),"取 消")]')


class MerchantManage(WebCommon):

    def search_merchant(self,merchant_name):
        self.input(merchant_name,merchant_name_element)
        self.click(search_btn_element)
        # # 查询到的商户名称
        # search_merchant = (By.XPATH, '//div[contains(text(),"%s")]'%name)
        # self.get_txt(*search_merchant)



    def create_merchant(self,merchant_name,username,corp,name,telephone):
        self.click(create_merchant_element)
        # self.into_div_alert()
        elements = self.locates(create_merchant_msg_element)
        print("elements长度：",len(elements))
        logger.info(f"账号username是{username}")
        logger.info(f"商户名称merchant_name{merchant_name}")
        #商户名称 存在则先删除
        merchant_name_select_sql = f"select * from merchant.merchant_base_info where account='{username}' or merchant_name='{merchant_name}';"
        merchant_name_del_sql = f"delete from merchant.merchant_base_info where account='{username}' or merchant_name='{merchant_name}';"
        merchant_user_select_sql = f"select * from merchant.merchant_user where account='{username}'"
        merchant_user_delete_sql = f"delete from merchant.merchant_user where account='{username}'"
        res1 = con_mysql("selectall", merchant_name_select_sql)
        res2 = con_mysql("selectall", merchant_user_select_sql)
        if res1:
            con_mysql("del", merchant_name_del_sql)
        if res2:
            con_mysql("del", merchant_user_delete_sql)

        self.input(merchant_name,elements[0])
        # elements[0].send_keys(merchant_name)
        #登录账号 存在则先删除
        self.input( username,elements[1])
        # elements[1].send_keys(username)
        #公司全称
        self.input(corp,elements[2])
        # elements[2].send_keys(corp)
        #姓名
        self.input(name,elements[3])
        # elements[3].send_keys(name)
        #手机号码
        self.input(telephone,elements[4])
        # elements[4].send_keys(telephone)
        # self.click(confirm_element)
        img_path= screen_path + "create_merchant.png"
        self.screenshot(img_path)
        self.allure_attach(img_path)
        self.confirm()
        self.sleep(2)
        # return self.search_merchant(merchant_name)

    def modify_merchant(self,merchant_name,corp,name,telephone):
        """只能修改公司全陈、姓名、手机号码"""
        #先找到该公司
        self.search_merchant(merchant_name)
        self.wait(3)
        self.click(modify_element)
        self.sleep(1)
        elements = self.locates(create_merchant_msg_element)
        print("elements长度：",len(elements))
        self.clear_input(corp,elements[2])
        # 姓名
        self.clear_input( name,elements[3])
        # 手机号码
        self.clear_input(telephone,elements[4])
        img_path = screen_path + "modify_merchant.png"
        self.screenshot(img_path)
        self.allure_attach(img_path)
        self.confirm()
        # return self.search_merchant(merchant_name)



