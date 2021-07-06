#coding=utf-8

from public_common.get_driver import get_driver
import pytest

if __name__=="__main__":
    #test_customer_manage
    pytest.main(["-sv","testcase/test_customer_manage.py"])
    # import shlex,subprocess
    # cmd = shlex.split("Nox.exe")
    # print(cmd)
    # p= subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    # print(p)
    # import os
    # cmd = "Nox"
    # d = os.popen(cmd,"r")
    # print(d.read())
    # d.close()




