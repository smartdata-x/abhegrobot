#!/usr/bin/python2.6  
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2015年4月12日

@author: pro
'''
from multiprocessing import Process,Pool,Pipe
from base.miglog import miglog
from movie.movie_mgr import MovieMgr

def UpdateMovie():
    #miglog.log().info("UpdateMovie")
    #批量获取电影信息
    mgr = MovieMgr()
    mgr.GetSpiderData()
    mgr.SpiderYoku()
    mgr.SubmitYokuInfo()

    
    
    
class MovieScheduler(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def star(self): # 启动一个进程
        '''
        pool = Pool(processes=1)
        result = pool.apply_async(UpdateMovie)
        result.get()
        pool.close()
        '''
        UpdateMovie()
        