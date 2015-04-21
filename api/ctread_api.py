#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8


'''
Created on 2015年2月23日

@author: pro

@summary: 天翼阅读HTTP接口
'''

from api.http_api import HttpApi

class CTReadHttp(object):
    
    def __init__(self):
        '''
        Constructor
        '''
        
    #天翼阅读类别搜索界面
    @classmethod
    def GetBookListByType(cls,tid):
        url = "http://wap.tyread.com/catelib.action?standColId="+tid
        return HttpApi.SpiderRequestMethodGet(url,"wap.tyread.com")