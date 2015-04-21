#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2015年2月20日

@author: pro
'''

from base.miglog import miglog
from api.http_spider import SpiderHttp
from api.ctread_api import CTReadHttp
from parser.parsing_ctread import ParserCTSearchHtml
from spider.ctread_orderbook import CTReadOrder

class CTReadSprider(object):
    '''
    classdocs
    用于爬取天翼阅读书籍
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__bookinfolist = [ 0 for i in range(0)] #书列表
        self.__userphonelist = [ 0 for i in range(0)] #用户号码列表
        
    def __get_userphone(self):#获取用户号码 500个号码
        self.__userphonelist = SpiderHttp.GetSpiderPhone()
        
    def __get_book_list(self):
        #
        self.__get_base_booktype("342","1")
        
        
    def __get_base_booktype(self,sid,tid): #获取书类别信息 #sid 天翼定义ID  tid爬虫定义ID
        data =  CTReadHttp.GetBookListByType(sid)
        parser = ParserCTSearchHtml()
        parser.feed(data)
        for element in parser.content_list:
            element.set_type(tid)
            #获取书的基本信息
            order = CTReadOrder("15319843161",element.get_bid())
            order.Start()
            
        
            
        
    def start(self):
        miglog.log().info("CTReadSpider Start")
        order = CTReadOrder("13346879578","100000226387426")
        order.Start()
        #self.__get_userphone()
        #self.__get_book_list()
        
        