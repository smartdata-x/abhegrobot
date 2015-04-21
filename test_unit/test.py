#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2015年1月13日

@author: mac
'''

#from book.collection_book import CollectionBook
from book.add_bookinfo import AddBookInfo
from parser.parsing_ctread import ParserCTSearchHtml
from parser.parsing_ctread import ParserCTBookInfoHtml
from parser.parsing_ctread import ParserCTChapterHtml
from parser.parsing_ctread import ParserCTContentHtml
from spider.ctread_sprider import CTReadSprider
from movie.gain_yoku_movie import GainYoKuMovie
from movie.movie_scheduler import MovieScheduler

from pub.config  import  SingletonConfig
import urlparse
import os
import urllib2
import httplib
import time
import sys

def TestIncludedBook():
    path = "/Users/mac/Downloads/book"
    dst ="/tmp/mac/Downloads/dst/book"
    #book_collection = CollectionBook(SingletonConfig().booksrc,SingletonConfig().bookdst,SingletonConfig().bookurl)
    #book_collection.Start()

def TestAddBookInfo():
    path = "/Users/mac/Downloads/bookinfo"
    print SingletonConfig().bookurl
    #book_add = AddBookInfo(path,SingletonConfig().bookurl,SingletonConfig().relativepic)
    #book_add.Start()
    
    
def TestParsingCTRead():
    #读取文件
    path = "/Users/pro/work/pj/ab/abhegrobot/data/description.txt"
    finput = open(path,'r')
    data = finput.read()
    finput.close()
    parser = ParserCTBookInfoHtml()
    parser.feed(data)
    
    #print parser.get_content()

    '''
    content_list = [ 0 for i in range(0)]
    content_list = parser.get_content_list()
    for element in content_list:
        print element.get_bid(),element.get_id(),element.get_name(),element.get_url()
    '''

def TestCTReadSpider():
    spider = CTReadSprider()
    spider.start()

def TestGainMovie():
    scheduler = MovieScheduler()
    scheduler.star()
    '''
    spider = GainYoKuMovie()
    url = "http://v.youku.com/v_show/id_XODQyMDkzMDk2.html"
    #spider.unit_movie("XODg5NjYwMTQ0")
    spider.unit_movie_url(url)
    '''
    
def ParserUrl():
    url1 = "http://120.26.118.139/getm3u8.ashx?ip=1019168418&ep=MQXSRwgfIbrf0fHD9eJxBIX2sUJs1wXKXB0%3d&vid=XNzk2NTI0MzMy"
    #url1 = "http://v.youku.com/player/getPlayList/VideoIDS/XNzk2NTI0MzMy/Pf/4/ctype/12/ev/1"
    url = urlparse.urlparse(url1)
    print url
    print url.scheme
    print url.netloc
    print url.path
    print len(url.query)
    
    
if __name__ == '__main__':
    reload(sys) 
    sys.setdefaultencoding('utf8')
    #TestIncludedBook()
    #TestAddBookInfo()
    #TestParsingCTRead()
    TestGainMovie()
    #ParserUrl()

