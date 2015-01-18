#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2015年1月14日

@author: mac
'''

import os
import chardet
import codecs
import json
import base.file as BaseFile
import base.util as BaseUtil
from base.miglog import miglog
from base.http import MIGHttpMethodPost
 
class CollectionBook(object):
    '''
    calssdocs
    '''
    
    def __init__(self,path,tar):
        '''
        Constructor
        '''
        self.path = os.path.abspath(path)
        self.relative_path = tar #相对路径
        self.target_path = tar #绝对路径
        self.host = "http://test.book.miglab.com"
        self.objs = []
        self.chapterlist = [0 for i in range(0)]
    
    #单线程单进程提交
    def Start(self):
        self.__WalkDir__()
        self.__Post_Collection__()
    
    
    #解析目录
    def __SplitDir__(self,path):
        subpath,name =  os.path.split(path)
        #获取小说名字
        temp,title = os.path.split(subpath)
        return subpath,name,title
    
    #批量提交信息给接口
    def __Post_Collection__(self):
        #print json.dumps(self.objs)
        #遍历20个以内为一提交
        post_queue = [0 for i in range(0)]
        for element in self.objs:
            post_queue.append(element)
            if(len(post_queue)>5):
                self.__HttpPostCollection__(json.dumps(post_queue))
                del post_queue[:]
            
    #请求服务端
    def __HttpPostCollection__(self,content):     
        url = "http://112.124.49.59/cgi-bin/buddha/robot/1/bookcollection.fcgi"
        host = "112.124.49.59"
        print "==========================="
        print content
        print "==========================="
        
        http = MIGHttpMethodPost(url,host)
        #data = {'uid':str(senderId),'touid':str(receiverId),'msg':msg}
        data= "uid=100008&token=727b5fb304e60ff10a3924cd0d25348e&chapter_list="+str(content)
        miglog.log().debug(data)
        http.HttpMethodPost(data=data,urlcode=0)
        


    #文件处理 如果UTF8直接拷贝非UTF8 进行转码
    def __CopyFile__(self,src,dst):
        finput = open(src,"r")
        str = finput.readline() + finput.readline()
        codetype = chardet.detect(str)["encoding"]  #检测编码方式 
        #print codetype
        if(codetype == "UTF-8"):
            BaseFile.CopyFile(src, dst)
            return True
            #删除源文件
        else:
            miglog.log().error(dst+":"+codetype)
            return False
        
    #组装json格式
    def __FormateJson__(self,obj):
        self.objs.append(obj)
        
    
    #分离后缀名
    def __SeparationExt__(self,name):
        starpos = name.find(".")
        return name[0:starpos]
    
    #遍历目录
    def __WalkDir__(self):
        extes = ('.txt','.jpg')
        self.chapterlist = BaseFile.WalkDir(self.path, extes)
        for element in self.chapterlist:
            subpath,t_chapter_name,book_name = self.__SplitDir__(element)
            chapter_name = self.__SeparationExt__(t_chapter_name)
            #剥离后缀名
            newbookname = BaseUtil.GetMD5(book_name)
            newname = BaseUtil.GetMD5(chapter_name)
            newtitle = BaseUtil.GetMD5(book_name)
            newsubpath = self.target_path+"/"+newtitle+"/"+newname+".txt"
            chapter_address = self.host+"/book/"+newtitle+"/"+newname+".txt"
            if(self.__CopyFile__(element, newsubpath)):
                obj = {"chapter_name":chapter_name,"hash_book_name":newbookname,"hash_chapter_name":newname,"chapter_address":chapter_address,"book_name":book_name}
                self.__FormateJson__(obj)
            
        
            
