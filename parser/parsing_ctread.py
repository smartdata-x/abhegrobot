#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2015年2月20日

@author: pro
'''

from HTMLParser import HTMLParser
from entity.data import CTReadBookItem
from entity.data import CTReadChapterItem

#解析天翼阅读单本订购页
class ParserOrderBook(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__pay_url = ""
    
    def get_pay_url(self):
        return "http://wap.tyread.com"+self.__pay_url
    
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if(attr[0] == "href" and attr[1].find("/bookdetail/")==0 ):
                self.__pay_url = attr[1]

        
#解析天翼阅读书的内容页面
class ParserCTContentHtml(HTMLParser):
    def __init__(self,bid,cid,name):
        HTMLParser.__init__(self)
        self.__bid = bid
        self.__cid = cid
        self.__name = name
        self.__content = ""
        self.__star = 0
        
    def get_content(self):
        return self.__content
        
    def handle_starttag(self, tag, attrs):
        '''
        print "tag:    ",tag
        for attr in attrs:
            print attr
        '''
        if(tag=="div"):
            for attr in attrs:
                if(attr[0]=="style" and attr[1]=="overflow:hidden;"):
                    self.__star=1
            
    def handle_data(self,data):
        if(self.__star==1):
            self.__content += data.lstrip()
            self.__content +="\n"
        
    def handle_endtag(self,tag):
        if(tag=="div"):
            self.__star = 0
        
         
#解析天翼阅读书的章节描述页
class ParserCTChapterHtml(HTMLParser):
    def __init__(self,bid):
        HTMLParser.__init__(self)
        self.__content_list = [ 0 for i in range(0)]
        self.__star = 0
        self.__chapter = 0
        self.__currpage = 0
        self.__pagecount = 0
        self.__index = 0 # 章节开发
        self.__bid = bid
        self.__xpagestar = 0
        self.__nextstar = 0
        self.__item = CTReadChapterItem()
        
        
    def get_content_list(self):
        return self.__content_list
    
    def get_currpage(self):
        return self.__currpage
    
    def get_pagecount(self):
        return self.__pagecount
    
    def handle_starttag(self, tag, attrs):
        
        '''  
        print "tag: ",tag
        
        for attr in attrs:
            print attr
        '''
        if(tag == "ul") :
            for attr in attrs:
                if(attr[1]=="list-lines"):
                    self.__star = 1
        elif (tag=="a" and self.__star ==1):
            self.__index = self.__index + 1
            self.__item.reset()
            for attr in attrs:
                if(attr[0]=="href"):
                    self.__chapter = 1
                    self.__item.set_id(self.__index)
                    self.__item.set_bid(self.__bid)
                    self.__item.set_url(attr[1])
        elif(tag == "div"):
            for attr in attrs:
                if(attr[1]=="xpage"):
                    self.__xpagestar = 1
        elif(tag == "span" and self.__xpagestar==1):
            for attr in attrs:
                self.__nextstar = self.__nextstar + 1
             
    
    def handle_data(self,data):
        #print "data: ",data
        if(self.__star ==1 and self.__chapter == 1):
            self.__item.set_name(data)
            items = CTReadChapterItem(self.__item.get_id(),self.__item.get_bid(),self.__item.get_name(),self.__item.get_url())
            self.__content_list.append(items)
            self.__chapter = 0
        
        elif(self.__xpagestar== 1 and self.__nextstar == 5):
            skey = "/"
            self.__xpagestar = 0
            self.__currpage = long(data[0:data.find(skey)])
            self.__pagecount = long(data[data.find(skey)+len(skey):len(data)])
            #self.currpage = long(data[0:data.find(skey)])
        
    def handle_endtag(self,tag):
        if(tag=="ul"):
            self.__star = 0

#解析天翼阅读书的描述页
class ParserCTBookInfoHtml(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.picandname = 0
        self.summarystar = 0
        self.authorstar = 0
        self.pic = ""
        self.name = ""
        self.summary = ""
        self.author = ""
        
    def handle_starttag(self, tag, attrs):
        
        if(tag=="div"):
            for attr in attrs:
                if(attr[1]=="mod clear"):
                    self.picandname = 2
                elif(attr[1]=="pic" and self.picandname==2):
                    self.picandname = 1
                elif(attr[1]=="txt-red"):
                    self.authorstar = 2
                    
        elif(tag=="img" and self.picandname == 1): #图片及名称
            for attr in attrs:
                if(attr[0]=="src"):
                    self.pic = attr[1]
                elif(attr[0]=="alt"):
                    self.name = attr[1]
        elif(tag=="span"):
            for attr in attrs:
                if(attr[1] =="con_desc"):
                    self.summarystar = 1
        elif(tag=="a" and self.authorstar==2):
            self.authorstar = 1
            
        
    
    def handle_data(self,data):
        print "data:    ",data
        if(self.summarystar==1):
            self.summary = data.lstrip()
        elif(self.authorstar==1):
            self.author = data.lstrip()
            self.authorstar = 0
                  
    def handle_endtag(self,tag):
        if(tag == "div") :
            self.picandname = 0
        if(tag == "span"):
            self.summarystar = 0
 
                
                    
#天翼阅读类别搜索返回页
class ParserCTSearchHtml(HTMLParser):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        HTMLParser.__init__(self)
        initial_value = 0
        self.star = 0
        self.content_list = [ initial_value for i in range(0)]
    
    def handle_starttag(self, tag, attrs):
        if(tag == "ul") :
            for attr in attrs:
                if(attr[1]=="list-lines border-t"):
                    self.star = 1
        elif (tag=="a" and self.star ==1):
            self.__create_ctitem(attrs)
          
    def handle_endtag(self,tag):
        if(tag == "ul") :
            self.star = 0
           
    
    def __create_ctitem(self,attrs):
        skey = "/bookdetail/"
        ekey = "/gobookinfo.html"
        for attr in attrs:
            item = CTReadBookItem(long(attr[1][attr[1].find(skey)+len(skey):attr[1].find(ekey)]))
            self.content_list.append(item)
            
        
        