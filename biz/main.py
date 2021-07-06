# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
import sys
sys.path.append("/public_common")
from common.get_driver import get_driver
class Test():
    def test01(self,name):
        self.name = name

    def test02(self):
        print(self.name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi(("PyCharm","23"))
    test = Test()
    print(test.test02())



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
