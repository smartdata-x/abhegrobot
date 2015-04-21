#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2015年2月22日

@author: pro
'''
from entity.baseinfo import BaseInfo

class SpiderPhoneNum(BaseInfo):
    
    def __init__(self):
        BaseInfo.__init__(self)
        self.phonelist = [ 0 for i in range(0)]
    
    
    
