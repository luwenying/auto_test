#coding:utf-8

from iflying.page.index import Index
from public_common.web_common import WebCommon
from public_common.read_data import yamlstr_to_tuple,get_yaml_data
from iflying.get_path import *



class Login(WebCommon):
    data = get_yaml_data(locate_data)

    def login(self,url):
        login_btn_element = yamlstr_to_tuple(self.data["login"]["login_btn_element"])
        self.open(url)
        self.wait(5)
        self.click(login_btn_element)
        self.sleep(6)
        return Index()

    def goto_register(self):
        goto_register_element = yamlstr_to_tuple(self.data["login"]["goto_register_element"])
        self.click(goto_register_element)
        return Register()



class Register():
    pass


