#coding:utf-8
import os.path
import time
from biz.get_path import *
from selenium.webdriver.common.by import By
from biz.page_object.login_page import Login
from public_common.get_driver import get_driver
import pytest
from biz.get_path import *
import yaml
from biz.common.get_logger import get_logger

@pytest.mark.skip("登录不需要执行")
class TestLogin():

    def setup_class(self):
        self.driver = get_driver()
        self.login = Login(self.driver)
        self.logger = get_logger()

    def teardown_class(self):
        self.login.close()

    @pytest.mark.parametrize("data",yaml.load(open(data_path+"login_data.yaml",encoding="utf-8"),Loader=yaml.FullLoader))
    def test_login(self,data):
        self.logger.info("开始登录，登录账号是:%s,登录密码是：%s"%(data["name"],data["pwd"]))
        self.login.login(data["name"],data["pwd"],data["sys"])
        self.login.sleep(2)
        self.login.logout()
        # try:
        #     error_txt = self.login.get_txt(*(By.XPATH,'//div[@class="el-form-item__error"]'))
        #     error_txt2 = self.login.get_txt(*(By.XPATH,'//*[@id="app"]/div/div[3]/div[2]/form/div[3]'))
        #     assert data["msg"] in (error_txt,error_txt2)
        # except:
        #     login_name = self.login.get_txt(*(By.XPATH, '//*[@id="app"]/div/header/div[2]/div[1]/span'))
        #     assert data["name"] in login_name








if __name__=="__main__":
    data = yaml.load(open(data_path+"login_data.yaml",encoding="utf-8"),Loader=yaml.FullLoader)
    print(data[0]["name"])
    print(data[0]["psd"])








