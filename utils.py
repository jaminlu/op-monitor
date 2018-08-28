# /usr/bin/env python
# -*- coding:utf-8 -*-
import json
import requests
from flask import g, redirect, session, abort, request
#from rrd import corelib

from rrd import config
from rrd.config import API_ADDR
import utils
import  os

#from rrd import corelib
#from rrd.utils import randbytes
#from model import  UserToken
#from rrd.utils.logger import logging

import ConfigParser
from rrd import config
def  get_config(service_conf, section=''):
    config = ConfigParser.ConfigParser()
    config.read(service_conf)

    conf_items = dict(config.items('falcon-api')) if config.has_section('falcon-api') else {}
    if section and config.has_section(section):
        conf_items.update(config.items(section))
    return conf_items

work_dir = os.path.dirname(os.path.realpath(__file__))
service_conf = os.path.join(work_dir, 'rrd/service.conf')
config = get_config(service_conf , 'falcon-api')
#print(config)

def login_user(name,password):
    params = {
        "name": name,
        "password": password,
    }

    r = requests.post("%s/user/login" %config.API_ADDR, data=params)

    if r.status_code != 200:
        raise Exception("%s : %s" %(r.status_code, r.text))

    j = r.json()
    ut = UserToken(j["name"], j["sig"])
    #set_user_cookie(ut, session)
    return ut

def set_user_cookie(user_token, session_):
    if not user_token:
	    return None
    session_[config.SITE_COOKIE] = "%s:%s" % (user_token.name, user_token.sig)
    return session_[config.SITE_COOKIE]


def auth_requests(method, *args, **kwargs):
    #from flask import g
    #if not g.user_token:
    #    raise Exception("no api token")

    name="root"
    password="ops_admin"
    user_token = login_user(name,password)

    headers = {
        "Apitoken": json.dumps({"name":user_token.name, "sig":user_token.sig})
    }

    #print headers 
    if not kwargs:
        kwargs = {}

    if "headers" in kwargs:
        headers.update(kwargs["headers"])
        del kwargs["headers"]

    if method == "POST":
        return requests.post(*args, headers=headers, **kwargs)
    elif method == "GET":
        return requests.get(*args, headers=headers, **kwargs)
    elif method == "PUT":
        return requests.put(*args, headers=headers, **kwargs)
    elif method == "DELETE":
        return requests.delete(*args, headers=headers, **kwargs)
    else:
        raise Exception("invalid http method")


def get_graph_history():
    data = {
	"step": 60,
  	"StartTime": 1527523200,
	"HostNames": ["ttw11999",],
	"EndTime": 1527537600,
	"Counters": ["iping.rtt.lost/point=tw06291"],
	"ConsolFun": "AVERAGE"
	}
    r = auth_requests("POST", API_ADDR + "/graph/history",data )
    return r.json()

def get_metric_list():
    r = auth_requests("GET", API_ADDR + "/metric/default_list")
    return r.json()

def get_endpoint_list():
    r = auth_requests("GET", API_ADDR + "/graph/endpoint")
    return r.status_code
    return r.json()
   

if __name__ == "__main__":
    print get_graph_history()
    #print login_user("root","ops_admin")
    #print get_metric_list()
    #print get_endpoint_list()
