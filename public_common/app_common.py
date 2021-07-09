#coding
from appium.webdriver import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AppCommon():

    def __init__(self,app_driver):
        self._driver = app_driver

    def locate(self, loc, value=None):
        if isinstance(loc, tuple):
            return self._driver.find_element(*loc)
        elif isinstance(loc, WebElement):
            loc: WebElement
            return loc.find_element(*value)
        else:
            return self._driver.find_element(loc, value)
