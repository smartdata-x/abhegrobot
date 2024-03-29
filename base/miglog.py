#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8

import logging
import datetime
'''
Created on 2014年6月6日

@author: Administrator
'''

class MIGLog(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        filename = 'robots_'+datetime.datetime.now().strftime('%b_%d_%y-%H')+'.log'
        #format_str = 'processid:%(process)d  %(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
        formate_str = '%(asctime)s [%(process)d] %(levelname)s [File:%(filename)s, Line:%(lineno)d]: %(message)s'
        logging.basicConfig(level=logging.DEBUG,
                format=formate_str,
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename= filename,
                filemode='a')
        ##控制台输出
        console = logging.StreamHandler()  
        console.setLevel(logging.INFO)
        console.setLevel(logging.DEBUG) 
        formatter = logging.Formatter(formate_str)  
        console.setFormatter(formatter)  
        # 将定义好的console日志handler添加到root logger  
        logging.getLogger('').addHandler(console)  
    
    def log(self):
        return logging
        
miglog = MIGLog()