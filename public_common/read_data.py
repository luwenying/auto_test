#coding:utf-8
import json
import time
from string import Template

import pymysql
import yaml
from iflying_manage.get_path import *
from public_common.get_logger import get_logger
from selenium.webdriver.common.by import By


logger = get_logger()
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


def con_mysql(env_name,key,sql):
    """
    key:selectall：返回全部
    key:selectone:返回一条
    key:update更新
    key:insert 插入
    key：delete或者del:删除
    """
    # print(db_config)
    data = get_yaml_data(db_config)[env_name]
    env = data["default"]
    db_data = data[env]
    # print("数据库环境是：",env)
    host = db_data["host"]
    username = db_data["username"]
    password = db_data["password"]
    db = db_data["db"]
    port = db_data["port"]
    con = pymysql.connect(host=host,user=username,passwd=password,db=db,port=port)
    #pymysql.cursors.DictCursor让返回的数据为key:value形式
    cur = con.cursor(pymysql.cursors.DictCursor)
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

def generate_screenshot_dirname():
    dirname = time.strftime("%Y-%m-%d",time.localtime())
    dirname_path = os.path.dirname(os.path.dirname(__file__))+"/iflying_manage/screenshot/"+dirname
    try:
        if not os.path.exists(dirname):
            os.makedirs(dirname_path)
        logger.info(f"{dirname_path}不存在，创建成功")
    except Exception:
        logger.info(f"{dirname_path}已存在，无需创建")
        return dirname_path




if __name__=="__main__":
    # sql = "select * from biz_script_recommend_relation where standard_script_name='$question' and merchant_id='1924093577040625664'".replace("$question","你好呀")
    # sql2 = "select id from km_domain where name='5555'"
    # res = con_mysql("km","selectone",sql2)
    # print(res)
    # data = get_yaml_data(db_config)
    # print(data)
    generate_dir_name()





