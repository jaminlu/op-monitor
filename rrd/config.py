# -*-coding:utf-8 -*-
import os

LOG_LEVEL = os.environ.get("LOG_LEVEL",'DEBUG')
# Falcon+ API
API_ADDR = os.environ.get("API_ADDR","http://公网IP:8090/api/v1")

SITE_COOKIE = os.environ.get("SITE_COOKIE","open-falcon-ck")


