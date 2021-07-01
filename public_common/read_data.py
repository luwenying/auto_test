#coding:utf-8
import pymysql
import yaml
from biz.get_path import *
from selenium.webdriver.common.by import By

def get_yaml_data(file_path):
    # menu = "商户管理"
    with open(file_path,"r",encoding="utf-8") as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
    # print(data)
    # print(data["menu_element"]%menu)
    return data

def yamlstr_to_tuple(data,**args):
    return eval(repr(data).replace('\'','').replace('\\',"'"))

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
    name='chenqh008'
    select_sql = f"select * from merchant_user where account='{name}'"
    res = con_mysql("selectone",select_sql)
    print(res)









if __name__=="__main__":
    # get_yaml_data(login_element_data)
    pass