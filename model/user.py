# /usr/bin/env python
# -*- coding:utf-8 -*-

class UserToken(object):
    def __init__(self, name, sig):
        self.name = name
        self.sig = sig
    
    def __repr__(self):
        return "<UserToken name=%s, sig=%s>"  % (self.name, self.sig)
    __str__ = __repr__
