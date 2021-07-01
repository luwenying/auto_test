#coding:utf-8
from biz.common.web_common import WebCommon
from selenium.webdriver.common.by import By
from biz.common.get_logger import get_logger
import time
from biz.common.get_logger import get_logger
from biz.common.read_data import get_yaml_data,yamlstr_to_tuple
from biz.get_path import *
from biz.page_object.merchant_page import MerchantManage
from biz.page_object.product_page import ProductManage
from biz.page_object.user_manage import UserManage

logger = get_logger()
_data = get_yaml_data(element_data)
logger.info(f"登录定位元素是：{_data}")

url = get_yaml_data(db_url)["url"]
username_loc = yamlstr_to_tuple(_data["username_loc"])
password_loc = yamlstr_to_tuple(_data["password_loc"])
login_btn_loc = yamlstr_to_tuple(_data["login_btn_loc"])
high_loc = yamlstr_to_tuple(_data["high_loc"])
continue_into = yamlstr_to_tuple(_data["continue_into"])
#退出系统
logout_name = yamlstr_to_tuple(_data["logout_name"])
logout_element = yamlstr_to_tuple(_data["logout_element"])
# print(high_loc)

# print(application_element)


class Login(WebCommon):
    logger = get_logger()
    _params = {}


    def login(self,name,pwd,sys_name):
        """登录系统"""

        # file_logger, console_logger = self.get_loggers()
        try:
            self.open(url)
            self.wait(3)
            self.input(name,username_loc)
            self.input(pwd,password_loc)
            self.click(login_btn_loc)
            self.sleep(2)
            # img_path = screen_path + "%s登录截图.png" % time.strftime("%Y%m%d%H%M%S")
            # self.screenshot(img_path)
            self.logger.info("登录账号：%s，登录密码：%s"%(name,pwd))

        except Exception as e:
            # console_logger.info("此链接不安全继续进入")
            self.click(high_loc)
            self.click(continue_into)
            self.wait(3)
            self.input(name,username_loc)
            self.input(pwd,password_loc)
            self.click(login_btn_loc)
            self.sleep(2)
            # img_path = screen_path + "%s登录截图.png" % time.strftime("%Y%m%d%H%M%S")
            # self.screenshot(img_path)
            self.logger.info("登录账号：%s，登录密码：%s" % (name, pwd))
            return self.__select_application(sys_name)

    def __select_application(self,sys_name):
        """选择系统"""
        self._params["sys_name"] = sys_name
        # application_element = (By.XPATH, f"//div[contains(text(),'{sys_name}')]")
        # sys_name = "商户管理中心"
        # application_element = yamlstr_to_tuple(_data["application_element"])
        _new_data = self.replace_yaml_variable(_data,self._params)
        application_element = yamlstr_to_tuple(_new_data["application_element"])
        self.sleep(1)
        # sys_name = '%s'%sys_name
        self.logger.info("登录的系统名称为：%s"%sys_name)
        self.click(application_element)
        self.sleep(1)
        img_path = screen_path + "%s进入系统截图.png" % time.strftime("%Y%m%d%H%M%S")
        self.screenshot(img_path)
        self.logger.info("进入系统截图为：%s"%img_path)


    def logout(self):
        self.hover(logout_name)
        self.click(logout_element)
        self.sleep(1)


    def left_menu_click(self,menu,second_menu):
        """点击左侧大菜单"""
        self._params["menu"] = menu
        self._params["second_menu"] = second_menu
        self.sleep(1)
        _new_data = self.replace_yaml_variable(_data, self._params)
        menu_element = yamlstr_to_tuple(_new_data["menu_element"])
        second_menu_element = yamlstr_to_tuple(_new_data["second_menu_element"])
        # menu_element = (By.XPATH,"//span[contains(text(),'%s')]"%menu)
        self.click(menu_element)
        self.sleep(1)
        return self.__left_second_menu_click(second_menu_element)

    def __left_second_menu_click(self,second_menu):
        """点击第二级菜单"""
        # self._params["second_menu"] = second_menu
        self.sleep(1)
        # second_menu_element = (By.XPATH, "//li[contains(text(),'%s')]" % second_menu)
        # _new_data = self.replace_yaml_variable(_data, self._params)
        # second_menu_element = yamlstr_to_tuple(_new_data["second_menu_element"])
        self.click(second_menu)
        self.sleep(1)
        # if second_menu=="商户管理":
        #     return MerchantManage(self.driver)
        # elif second_menu=="产品管理":
        #     return ProductManage(self.driver)
        # elif second_menu=="用户管理":
        #     return UserManage(self.driver)




if __name__=="__main__":
    pass
    # import time
    # img_path = screen_path+"%s登录截图.png"%time.strftime("%Y%m%d%H%M%S")
    # print(img_path)
    #
    # from common.get_driver import get_driver
    # driver = get_driver()
    # login = Login(driver)
    # login.open("https://admintest.robot.com/#/login")
    # time.sleep(2)
    # login.screenshot(img_path)




