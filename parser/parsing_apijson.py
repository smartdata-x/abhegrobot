#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2015年2月22日

@author: pro
'''
import json

def ParsingApiJson(content):
    try:
        dic = eval(content)
        result = ""
        object = json.loads(content)
        if(object["status"] == 1):
            if(dic.has_key("result")):
                return 1,object["result"]
        else:
            return 0,result
    except:
        return 0,None
    