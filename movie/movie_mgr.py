#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2015年4月19日

@author: pro
'''

import json
import base64
import api.http_spider as SpiderApi
from movie.gain_yoku_movie import GainYoKuMovie
from entity.data import YouKuUnit

class MovieMgr(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.list = [ 0 for i in range(0)] #存请求数据
        self.post_list = [0 for i in range(0)] #提交数据
        
    def __SetUnitObj__(self,dic):
        for obj in dic:
            self.list.append(obj)
        
    def GetSpiderData(self):
        pos = 0
        count = 10
        while True:
            dic = SpiderApi.SpiderHttp.GetSpiderYoKuToken(pos,count)
            pos = pos + count
            if(dic==None or len(dic)<count):
                break
            self.__SetUnitObj__(dic)
            del dic[:]
        
        if(dic <> None and len(dic)<count and len(dic)>0 ):
            self.__SetUnitObj__(dic)
            del dic[:]
    
    def SpiderYoku(self):
        spider = GainYoKuMovie()
        for obj in self.list:
            unit = YouKuUnit(obj["id"],obj["token"])
            #print unit.get_token()
            spider.unit_movie_url(unit)
            self.post_list.append(unit.dict_dump())
            
    def SubmitYokuInfo(self):
        for unit in self.post_list:
            #base64 编码
            SpiderApi.SpiderHttp.UpdateMovieYoku(json.dumps(unit))
            