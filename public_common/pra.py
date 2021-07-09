#coding:utf-8

import os
f = os.popen("ipconfig","r")
print(f.read())