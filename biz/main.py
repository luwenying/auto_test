# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
import sys
sys.path.append("/public_common")
from common.get_driver import get_driver

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.maximize_window()
    driver.get("https://admintest.robot.com/#/login")
    driver.save_screenshot("login.png")
    driver.window_handles()
    driver.current_window_handle()
    driver.switch_to.window()
    driver.find_element()
    driver.execute_script()
    if isinstance(name,tuple):
        p(*name)
    else:
        print("不是元组格式")

def p(name,age):
    print(name)
    print(age)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(("PyCharm","23"))
    # print(isinstance(('PyCharm',"12"),tuple))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
