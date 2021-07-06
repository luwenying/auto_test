#coding:utf-8
import json
from string import Template

import pymysql
import yaml
from biz.get_path import *
from selenium.webdriver.common.by import By

from iflying.get_path import *


def get_yaml_data(file_path):
    # menu = "商户管理"
    with open(file_path,"r",encoding="utf-8") as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
    # print(data)
    # print(data["menu_element"]%menu)
    return data

def yamlstr_to_tuple(data,**args):
    return eval(repr(data).replace('\'','').replace('\\',"'"))

def replace_yaml_variable(yaml_data,params:dict):
    raw = json.dumps(yaml_data)
    print(type(raw))
    for key,value in params.items():
        raw =raw.replace(f"${{{key}}}",value)
    new_data = json.loads(raw)
    return new_data

def replace_variable(data:str,**kwargs):
    if isinstance(data,str):
        data = data
    else:
        data = json.dumps(data)
    new_data = json.loads(Template(data).substitute(**kwargs))
    print("__替换后的数据为：",new_data)
    return new_data


def con_mysql(key,sql):
    """
    key:selectall：返回全部
    key:selectone:返回一条
    key:update更新
    key:insert 插入
    key：delete或者del:删除
    """
    data = get_yaml_data(db_url)
    host = data["host"]
    username = data["username"]
    password = data["password"]
    db = data["db"]
    con = pymysql.connect(host=host,user=username,passwd=password,db=db)
    cur = con.cursor()
    cur.execute(sql)
    if key=="selectall":
        return cur.fetchall()
    elif key=="selectone":
        return cur.fetchone()
    elif key in ("update","insert","delete","del"):
        con.commit()
    else:print("key不对")
    cur.close()
    con.close()





if __name__=="__main__":
    # sql = "INSERT INTO mkt_product VALUES (1908653076194000902, 'PRODUCT_CODE', '20210618004product', 'NORMAL', '1', 1864957990774112257, 'NORMAL', '2021-06-18 09:13:54', 0, 0, '2021-06-07 09:44:57');"
    # con_mysql("insert",sql)
    # name='chenqh008'
    # select_sql = f"select * from merchant_user where account='{name}'"
    # res = con_mysql("selectone",select_sql)
    # print(res)
    data = get_yaml_data(language_manage_element)
    print(type(data))
    # print(json.dumps(data))
    data1 = data["add_industry_name_select_element"]
    print(data1)
    print(type(data1))
    re_data1 = data1.replace("$add_industry_name","你好")
    print(re_data1)
    new_data = replace_variable(data1,add_industry_name="你好")

    # print(type(new_data))
    # data = {"name": (By.XPATH,'//span[text()="$add_industry_name"]')}
    # print(data["name"])
    # newdata = replace_variable(data["name"],add_industry_name="你好")
    # name = yamlstr_to_tuple(newdata["name"])
    # print(newdata)
    # # print(name)






