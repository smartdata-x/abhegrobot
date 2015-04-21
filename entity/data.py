#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2015年2月20日

@author: pro
'''

import json

#电信章节格式
class CTReadChapterItem:
    def __init__(self,cid=0,bid=0,name="",url=""):
        self.reset()
        self.__id = cid
        self.__bid = bid
        self.__name = name
        self.__url = url
        
    
    def reset(self):
        self.__id = 0
        self.__bid = 0
        self.__name = ""
        self.__url = ""
        
    def get_bid(self):
        return self.__bid
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_url(self):
        return self.__url
    
    def set_bid(self,bid):
        self.__bid = bid
    
    def set_id(self,cid):
        self.__id = cid
        
    def set_name(self,name):
        self.__name = name
    
    def set_url(self,url):
        self.__url = url
        
        
#电信书籍格式
class CTReadBookItem:
    def __init__(self,bid):
        self.__id = bid #书ID
        self.__name = "" #书名
        self.__author = "" #作者
        self.__type = "" #类别
        self.__head = "" #封面
        self.__summary = "" #书籍介绍
        self.__hash_name = "" #HASH 名 避免重复出现
        self.__desc_url = "http://wap.tyread.com/bookdetail/"+str(bid)+"/gobookdescription.html" #自行构建章节详细地址
        self.__info_url = "http://wap.tyread.com/bookdetail/"+str(bid)+"/gobookinfo.html" #自行构建书籍详情地址
        
    def get_bid(self):
        return self.__id
    
    def set_type(self,type):
        self.__type = type
        
#优酷视频单元格式
class YouKuUnit:
    def __init__(self,vid,token,name="",logo="",desc="",play_url=""):
        self.__id = vid
        self.__token = token
        self.__name = name
        self.__logo = logo
        self.__desc = desc
        self.__play_url = play_url
    
    def set_token(self,token):
        self.__token = token
    
    def set_name(self,name):
        self.__name = name
        
    def set_logo(self,logo):
        self.__logo = logo
    
    def set_desc(self,desc):
        self.__desc = desc
    
    def set_play_url(self,url):
        self.__play_url = url
    
    def get_token(self):
        return self.__token
    
    def dump(self):
        print self.__id,self.__logo,self.__name,self.__play_url,self.__token
    
    def dict_dump(self):
        dict = {}
        dict["id"] = int(self.__id)
        dict["token"] = str(self.__token)
        dict["name"] = str(self.__name)
        dict["logo"] = str(self.__logo)
        dict["desc"] = str(self.__desc)
        dict["url"] = str(self.__play_url)
        return dict
        

