#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8
'''
Created on 2015年1月13日

@author: mac
'''

from base.miglog import miglog
import os
import shutil
def WalkDir(dir,extes,file_callback=None):
    content_list = [0 for i in range(0)]
    for root, dirs, files, in os.walk(dir):
        for f in files:
            ext = os.path.splitext(f)[1]
            if  ext  in extes:        
                file_path = os.path.join(root, f)
                content_list.append(file_path)
    return content_list

#检测目录是否存在 不存在创建ß
def CheckFileDir(dst_dir):
    path,file = os.path.split(dst_dir)
    if not os.access(path, os.F_OK):
        #创建
        os.makedirs(path)
        
def CopyFile(src_file,dst_file):
    if not os.access(src_file, os.F_OK):
        miglog.log().error(src_file+" does not exist")
    #检测目录是否存在
    CheckFileDir(dst_file)
    shutil.copyfile(src_file, dst_file)
    
    
        