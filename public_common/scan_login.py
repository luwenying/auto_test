#coding:utf-8
from appium import webdriver
from selenium import webdriver
import time
from time import sleep
import os

from selenium.webdriver.common.by import By
from public_common.get_app_driver import get_app_driver
from public_common.web_common import WebCommon


class ScanLogin(WebCommon):


    def scan_login(self):
        # 微信登录
        wechat_login_element = (By.ID, 'com.tencent.wework:id/a0a')
        #选择公司
        corp_name_element = (By.XPATH, "//*[@text='火星公司']")
        #点击进入
        into_element = (By.ID, 'com.tencent.wework:id/c8y')
        #点击加号
        plus_element = (By.XPATH, '//android.widget.TextView[@resource-id="com.tencent.wework:id/hcg" and @index="0"]')
        #点击扫一扫
        scan_element = (By.XPATH, "//*[@text='扫一扫']")
        #点击相册
        picture_element = (By.ID,"com.tencent.wework:id/hcg")
        #选择相册
        select_picture_elemet = (By.ID,"com.tencent.wework:id/k1")
        #点击确定
        confirm_element = (By.ID,"com.tencent.wework:id/hcn")
        #点击确认登录
        confirm_login_element = (By.XPATH,"//*[@text='确认登录']")

        self.wait_element_visible(wechat_login_element)
        self.click(wechat_login_element)
        self.wait_element_visible(corp_name_element)
        self.click(corp_name_element)
        self.wait_element_visible(into_element)
        self.click(into_element)
        self.wait_element_visible(plus_element)
        self.click(plus_element)
        self.wait_element_visible(scan_element)
        self.click(scan_element)
        self.wait_element_visible(picture_element)
        self.click(picture_element)
        self.wait_element_visible(select_picture_elemet)
        self.click(select_picture_elemet)
        self.wait_element_visible(confirm_element)
        self.click(confirm_element)
        self.wait_element_visible(confirm_login_element)
        self.click(confirm_login_element)


def execute_dos(cmd):
    f = os.popen(cmd,"r")
    print(f)
    # f.close()


if __name__=="__main__":
    # execute_dos("nox")
    # time.sleep(15)
    # execute_dos("adb connect 127.0.0.1:62001")
    # driver = webdriver.Chrome()
    # driver.get("https://iflying-manage-dev.zhilingsd.com/#/login")
    # time.sleep(2)
    # driver.find_element("xpath",'//span[text()=" 登录 "]').click()
    # time.sleep(1)
    # execute_dos(r"del F:\webUI\iflying\screenshot/二维码.png")
    # driver.save_screenshot(r"F:\webUI\iflying\screenshot/二维码.png")
    # #打开夜神模拟器
    # try:
    #     execute_dos(r"adb shell rm /storage/emulated/0/Pictures/Screenshots/二维码.png")
    # except Exception as e:
    #     print(e)
    # finally:
    #     execute_dos(r"adb push F:\webUI\iflying\screenshot/二维码.png  /storage/emulated/0/Pictures/Screenshots/二维码.png")
    get_app_driver = get_app_driver()
    scan_login = ScanLogin(get_app_driver)
    scan_login.scan_login()


