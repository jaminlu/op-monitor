# /usr/bin/env python
# -*- coding:utf-8 -*-
from api import jsonrpc
from utils import config
from rrd.config import API_ADDR
from utils import auth_requests
import requests
headers = {"Content-Type": "application/json"}
data = {
    "jsonrpc": "2.0",
    "id": "1",
}

def get_url():
    return "http://%s/api" % config['api_host']

def test_api():
    data['method']="serverlist.history"
    data['params']={}
    print get_url()
    r=requests.post(get_url(), headers=headers, json=data)
    print r.text


if __name__=='__main__':
    test_api()