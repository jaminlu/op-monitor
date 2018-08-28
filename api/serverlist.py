#!/usr/bin/env python
#coding:utf-8
from auth import auth_requests
from rrd.config import API_ADDR
from . import jsonrpc, app
import json


@jsonrpc.method('serverlist.history')
def get_netinfo(**kwargs):
    data = {
        "step": 60,
        "StartTime": 1527523200,
        "HostNames": ["ttw11999", ],
        "EndTime": 1527537600,
        "Counters": ["iping.rtt.lost/point=tw06291"],
        "ConsolFun": "AVERAGE"
    }
    r = auth_requests("POST", API_ADDR + "/graph/history", data)
    return r.json()
    #return json.dumps({'code':1,'errmsg':'create cabinet fail'})

