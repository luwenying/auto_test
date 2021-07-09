#coding:utf-8
from appium import webdriver


def get_app_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.2'
    desired_caps['deviceName'] = '127.0.0.1:62001'
    desired_caps['appPackage'] = 'com.tencent.wework'
    desired_caps['appActivity'] = '.login.controller.LoginWxAuthActivity'
    desired_caps['noReset'] = 'true'
    desired_caps["dontStopAppOnset"] = "true"
    desired_caps["skipDeviceInitialization"] = "true"
    app_driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    return app_driver