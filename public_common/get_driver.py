#coding:utf-8
from selenium import webdriver


def get_driver(browser="Chrome"):
    try:
        return getattr(webdriver,browser)()
    except Exception as e:
        print("实例化浏览器出现异常：%s"%e)
