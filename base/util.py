#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2014年5月31日

@author: kerry
'''

import json
import uuid
import hashlib

def GetMac():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

def GetMD5(content):
    key = hashlib.md5()
    key.update(content)
    return key.hexdigest()

        
    