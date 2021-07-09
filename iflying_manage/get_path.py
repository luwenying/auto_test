#coding:utf-8
import os

base_dir = os.path.dirname(__file__)
log_config_path = base_dir+"/config/log.conf"
log_path = base_dir+"/log/biz.log"
screen_path = base_dir+"/screenshot/"
# print(base_dir)
data_path = base_dir+"/data/"
login_element = data_path+"login_element.yaml"
all_data = data_path+"all_data.yaml"
login_cookies_data = data_path+"cookies.json"
customer_manage_element = data_path+"customer_manage_element.yaml"
language_manage_element = data_path+"language_manage_element.yaml"
corp_manage_element = data_path +"corp_manage_element.yaml"
db_config = data_path+"db.yaml"