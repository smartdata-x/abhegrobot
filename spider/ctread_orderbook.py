#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2015年2月23日

@author: pro

@summary: 模拟订购单本书
'''

from api.http_api import HttpApi
from parser.parsing_ctread import ParserOrderBook

class CTReadOrder(object):
    '''
    classdocs
    '''


    def __init__(self, phone,bookid):
        '''
        Constructor
        '''
        self.__phone = phone
        self.__bookid = bookid
        self.__url = "http://wap.tyread.com/bookdetail/"+str(bookid)+"/gobookinfo.html?is_ctwap=1"
        self.__pay_url = ""
        
    def HttpHeader(self,host,referer):
            headers = {
                       "Host":host,
                       "Proxy-Connection":"keep-alive",
                       "X-Requested-With":"com.android.browser",
                       "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                       "User-Agent":"Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; ZTE N900 Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
                       "Accept-Encoding":"gzip, deflate",
                       "x-wap-profile":"http://www.zte.com.cn/mobile/uaprof/N900.xml",
                       "Accept-Language":"zh-CN, en-US",
                       "Accept-Charset":"utf-8, iso-8859-1, utf-16, *;q=0.7",
                       "X-Up-Calling-Line-ID":self.__phone,
                       "HTTP_X_UP_CALLING_LINE_ID":self.__phone,
                       "X-ClientIP":"10.234.87.168",
                       "X-forwarded-for":"10.16.3.248",
                       "Referer":referer
            }
            return headers
        
    def CTReadLogin(self):
        data =  HttpApi.SpiderRequestMethodGet(self.__url, "wap.tyread.com", None, self.HttpHeader("wap.tyread.com", "http://wap.tyread.com"), None)
        parser = ParserOrderBook()
        parser.feed(data)
        self.__pay_url =  parser.get_pay_url()
    
    def CTReadOrder(self):
        data = HttpApi.SpiderRequestMethodGet(self.__pay_url, "wap.tyread.com", None, self.HttpHeader("wap.tyread.com", self.__url), None)
        #print data
        
    def CTReadBatchOrder(self):
        url = "http://wap.tyread.com/batchSubscribe.action?is_ctwap=1&bookId=100000226423411&subscribeChapters=100&readcurrencyprice=8&chargeMode=3&fromModule=X-bookmulu-buy-100chapter"
        data = HttpApi.SpiderRequestMethodGet(url, "wap.tyread.com", None, self.HttpHeader("wap.tyread.com",self.__pay_url), None)
        
    
    def CTReadConfirmOrder(self):
        url = "http://wap.tyread.com/confirmBatchSubscribe.action?is_ctwap=1&"
        lasturl = "http://wap.tyread.com/batchSubscribe.action?is_ctwap=1&bookId=100000226423411&subscribeChapters=100&readcurrencyprice=8&chargeMode=3&fromModule=X-bookmulu-buy-100chapter"
        data = HttpApi.SpiderRequestMethodGet(url, "wap.tyread.com", None, self.HttpHeader("wap.tyread.com",lasturl), None)
        print data
        
    def Start(self):
        self.CTReadLogin()
        self.CTReadOrder()
        self.CTReadBatchOrder()
        self.CTReadConfirmOrder()
        
        