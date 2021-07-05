#coding:utf-8

from iflying.page.index import Index
from public_common.web_common import WebCommon
from public_common.read_data import yamlstr_to_tuple,get_yaml_data
from iflying.get_path import *



class Login(WebCommon):
    data = get_yaml_data(login_element)


    def login(self,url):
        login_btn_element = yamlstr_to_tuple(self.data["login"]["login_btn_element"])
        self.open(url)
        self.click(login_btn_element)
        self.sleep(8)
        # self.write_cookies_to_file(login_cookies_data)
        self.sleep(1)
        return Index(self._driver)

    def goto_register(self):
        goto_register_element = yamlstr_to_tuple(self.data["login"]["goto_register_element"])
        self.click(goto_register_element)
        return Register()

    def cookie_login(self,url):
        self.open(url)
        self.add_cookies(login_cookies_data)
        return Index(self._driver)






class Register():
    pass


if __name__=="__main__":
    pass



