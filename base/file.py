#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2015年1月13日

@author: mac
'''

import os
def WalkDir(dir,file_callback=None):     
    for root, dirs, files, in os.walk(dir):
        for f in files:
            ext = os.path.splitext(f)[1]
            if  ext  in ('.png', '.jpg'):              
                print "filename:"+f         
                file_path = os.path.join(root, f)
                #type,doc = SplitDir(file_path)   
                #if file_callback: file_callback(type,doc,file_path)
                #print "===============" 