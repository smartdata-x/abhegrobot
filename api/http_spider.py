#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2015年2月22日

@author: pro

@summary: 爬虫所需接口
'''

from api.http_api import HttpApi
import urllib

class SpiderHttp(object):
    
    uid = "10000"
    token = "eb722ea6829bde8d2742101073681c65"
    def __init__(self):
        '''
        Constructor
        '''
    
    #获取号码
    @classmethod 
    def GetSpiderPhone(cls):
        path = "robot/1/spiderphone.fcgi?uid="+cls.uid
        dic  = HttpApi.RequestMethodGet(path)
        return dic["list"]
    
    #获取优酷信息
    @classmethod
    def GetSpiderYoKuToken(cls,pos=0,count=10):
        path = "robot/1/gainmovie.fcgi?uid="+cls.uid+"&token="+cls.token+"&from="+str(pos)+"&count="+str(count)
        dic = HttpApi.RequestMethodGet(path)
        if(dic.has_key("list")):
            return dic["list"]
        else:
            return None
    
    #更新优酷信息
    @classmethod
    def UpdateMovieYoku(cls,content):
        path = "robot/1/updatemovie.fcgi"
        #content 中有中文需进行中urlcode编码
        m = {'unit':content}
        data = "uid="+cls.uid+"&token="+cls.token+"&"+urllib.urlencode(m)
        HttpApi.RequstMethodPost(path,data)
        
        
        
