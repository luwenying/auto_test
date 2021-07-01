#coding:utf-8
import json
import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from biz.common.get_logger import get_logger
from selenium.webdriver.common.action_chains import ActionChains

class WebCommon():
    _alert_list = [((By.XPATH, '//span[contains(text(),"确 认")]'), (By.XPATH, '//span[contains(text(),"取 消")]'))]
    logger = get_logger()

    def __init__(self,driver):
        self.driver = driver

    def open(self,url):
        self.driver.get(url)

    def locate(self,loc,value=None):
        if isinstance(loc, tuple):
            return self.driver.find_element(*loc)
        elif isinstance(loc,WebElement):
            loc: WebElement
            return loc.find_element(*value)
        else:
            return self.driver.find_element(loc,value)

        # try:
        # except Exception:
        #     self.logger.info("有弹窗，走关闭弹窗路径")
        #     for ele in self._alert_list:
        #         self.click(ele)


    def locates(self,loc,value=None):
        if isinstance(loc, tuple):
            return self.driver.find_elements(*loc)
        elif isinstance(loc, WebElement):
            loc: WebElement
            return loc.find_elements(*value)
        else:
            return self.driver.find_elements(loc, value)

    def click(self,loc,value=None):
        if isinstance(loc, WebElement):
            loc: WebElement
            loc.click()
        else:
            self.locate(loc,value).click()

    def input(self,txt,loc,value=None):
        if isinstance(loc,WebElement):
            loc: WebElement
            loc.send_keys(txt)
        else:
            self.locate(loc, value).send_keys(txt)

    def clear_input(self,txt,loc,value=None):
        if isinstance(loc,WebElement):
            loc: WebElement
            loc.clear()
            loc.send_keys(txt)
        else:
            elem = self.locate(loc,value).clear()
            elem.send_keys(txt)

    def element_input(self,txt,element):
        element.send_keys(txt)

    def element_click(self,element):
        element.click()


    def get_txt(self,loc,value=None):
        if isinstance(loc,WebElement):
            loc: WebElement
            return loc.text
        else:
            elem= self.locate(loc,value)
            return elem.text

    def wait(self,num):
        self.driver.implicitly_wait(num)

    def sleep(sel,num):
        time.sleep(num)

    def into_frame(self,loc,value=None):
        if isinstance(loc,WebElement):
            self.driver.switch_to.frame(loc)
        else:
            elem = self.locate(loc,value)
            self.driver.switch_to.frame(elem)

    def max(self):
        self.driver.maximize_window()

    def close(self):
        self.driver.close()

    def screenshot(self,img_path):
        self.driver.save_screenshot(img_path)

    def into_div_alert(self):
        window_list = self.driver.window_handles
        # current_window = self.driver.current_window_handle
        self.driver.switch_to.window(window_list[len(window_list)-1])
        # for window in range(len(window_list)+1):
        #     if window_list[window]!= current_window:
        #         self.driver.switch_to.window(window_list[window])

    def confirm(self):
        # 确认按钮
        # confirm_element_list = [
        #     (By.XPATH, '//span[contains(text(),"确 认")]'),
        #     (By.XPATH, '//span[contains(text(),"确认")]')
        # ]
        # for confirm_element in confirm_element_list:
        #     self.click(confirm_element)
        try:
            confirm_element = (By.XPATH, '//span[contains(text(),"确 认") ]')
            self.click(confirm_element)
        except Exception as e:
            confirm_element = (By.XPATH, '//span[contains(text(),"确认") ]')
            self.click(confirm_element)

            # raise e


    def cancel(self):
        # 取消按钮
        concel_element = (By.XPATH, '//span[contains(text(),"取 消")]')
        self.click(concel_element)

    def hover(self,loc,value=None):
        if isinstance(loc,WebElement):
            ActionChains(self.driver).move_to_element(loc).perform()
        else:
            ActionChains(self.driver).move_to_element(self.locate(loc, value)).perform()


    def execute_js(self,js):
        self.driver.execute_script(js)

    def execute_js_click(self,loc,value=None):
        if isinstance(loc,WebElement):
            self.driver.execute_script("arguments[0].click()",loc)
        else:
            self.driver.execute_script("arguments[0].click()",self.locate(loc,value))

    def allure_attach(self,img_path):
        """在allure报告中插入截图"""
        with open(img_path,"rb") as f:
            content = f.read()
            allure.attach(content,attachment_type=allure.attachment_type.PNG)

    def replace_yaml_variable(self,yaml_data,params:dict):
        raw = json.dumps(yaml_data)
        print(type(raw))
        for key,value in params.items():
            raw =raw.replace(f"${{{key}}}",value)
        new_data = json.loads(raw)
        return new_data








if __name__=="__main__":
    from public_common.get_driver import get_driver
    from biz.common.read_data import get_yaml_data
    from biz.get_path import *
    import yaml
    driver = get_driver()
    web = WebCommon(driver)
    _params = {}
    sys_name = "商户管理中心"
    menu = "产品管理"
    second_menu = "产品管理"
    _params["sys_name"] = sys_name
    _params["menu"] = menu
    _params["second_menu"] = second_menu
    _data = get_yaml_data(element_data)
    data = web.replace_yaml_variable(_data,_params)
    print(data["application_element"])
    print(data["menu_element"])
    print(data["second_menu_element"])






