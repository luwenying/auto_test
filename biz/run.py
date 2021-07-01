#coding:utf-8
import pytest
import time


if __name__=="__main__":
    #test_user_manage
    time = time.strftime("%Y%m%d%H%M%S")
    pytest.main(["-sv","test_case/test_user_manage.py","--alluredir=./report/"])
    # import subprocess,shlex
    # cmd = shlex.split("ipconfig")
    # p = subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    # print(p)
