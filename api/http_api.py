#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2015年2月22日

@author: pro

@summary: http基础接口
'''

from base.http import MIGHttpMethodGet,MIGHttpMethodPost
from base.miglog import miglog
from pub.config import SingletonConfig
import urlparse
import json

import parser.parsing_apijson as parser

class HttpApi(object):
    def __init__(self):
        pass
    
    @classmethod
    def RequestMethodGet(cls,path):
        host = SingletonConfig().apihost
        url = SingletonConfig().apiurl+path
        http = MIGHttpMethodGet(url,host)
        http.HttpMethodGet()
        status,baseinfo = parser.ParsingApiJson(http.HttpGetContent())
        if(status==1):
            return baseinfo
        
    @classmethod
    def RequstMethodPost(cls,path,data):
        host = SingletonConfig().apihost
        url = SingletonConfig().apiurl+path
        http = MIGHttpMethodPost(url,host)
        http.HttpMethodPost(data)
        status,baseinfo = parser.ParsingApiJson(http.HttpGetContent())
        if(status==1):
            return baseinfo
    '''    
    @classmethod
    def SpiderRequestMethodGet(cls,path,host,port=None,header=None,cookies=None):
        http = MIGHttpMethodGet(path,host)
        http.HttpMethodGet(header,cookies,port)
        return http.HttpGetContent()
    '''
        
    @classmethod
    def SpiderRequestMethodGet(cls,url,port=None,header=None,cookies=None):
        #解析
        parse = urlparse.urlparse(url)
        if(len(parse.query)==0):
            neturl = parse.path
        else:
            neturl = parse.path+"?"+parse.query
        http = MIGHttpMethodGet(neturl,parse.netloc)
        http.HttpMethodGet(header,cookies,port)
        return http.HttpGetContent()
        
        
        