#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2015年1月18日

@author: mac
'''
import os
import codecs
import urllib
import json
import base.file as BaseFile
import base.util as BaseUtil
from base.http import MIGHttpMethodPost
from base.miglog import miglog

#封面和介绍
class AddBookInfo(object):
    '''
    calssdocs
    '''
    
    def __init__(self,path,pic,tar):
        self.picurl = pic
        self.path = os.path.abspath(path)
        self.relative_path = tar #相对路径
        self.target_path = tar #绝对路径
        #
        self.bookinfodic = {}
    #单线程单进程提交
    def Start(self):
        self.__WalkDir__()
        self.__PostCollection_()
        
        
        #请求服务端
    def __HttpPostCollection__(self,content):     
        url = "http://112.124.49.59/cgi-bin/buddha/robot/1/bookcollection.fcgi"
        host = "112.124.49.59"
        http = MIGHttpMethodPost(url,host)
        #data = {'uid':str(senderId),'touid':str(receiverId),'msg':msg}
        data= "uid=100008&token=727b5fb304e60ff10a3924cd0d25348e&"+str(content)
        miglog.log().debug(data)
        http.HttpMethodPost(data=data,urlcode=0)
        
    def __PostCollection_(self):
        #遍历提交20个为一提交
        post_queue = [0 for i in range(0)]
        for k in self.bookinfodic:
            post_queue.append(self.bookinfodic[k])
            if(len(post_queue)>1):
                content = {'bookinfo_list':json.dumps(post_queue)}
                self.__HttpPostCollection__(json.dumps(post_queue))
                del post_queue[:]
    #解析类别，小说名,图片
    def __SplitDir__(self,path):
        subpath,name =  os.path.split(path)
        subpath,title = os.path.split(subpath)
        subpath,type = os.path.split(subpath)
        return type,name,title
    
    #图片处理
    def __GetCover__(self,bookname,picname,path):
        ext = os.path.splitext(path)[1]
        relative_path = self.relative_path + "/" + bookname + "/" + picname + ext
        dst = self.target_path + relative_path #绝对路径
        BaseFile.CopyFile(path, dst)
        return relative_path
    
    #文字处理
    def __GetIntroContent__(self,path):
        #读取内容
        f = codecs.open(path,'r','utf-8')
        s = f.readlines()
        f.close()
        return ','.join(s)

        
    
    def __AddBookInfo__(self,key,book_name,content,type):
        newbookname = BaseUtil.GetMD5(book_name)
        newcontentname = BaseUtil.GetMD5(content)
        if(self.bookinfodic.has_key(key)):
            if(os.path.splitext(content)[1]=='.txt'):
                self.bookinfodic.get(key).setdefault("intro",self.__GetIntroContent__(content))
            else:
                self.bookinfodic.get(key).setdefault("cover",self.__GetCover__(newbookname, newcontentname, content))
        else:
            dic = {}
            dic.setdefault("type",type)
            dic.setdefault("name",book_name)
            #通过后缀名判断
            if(os.path.splitext(content)[1]=='.txt'):
                dic.setdefault("intro",self.__GetIntroContent__(content))
            else:
                dst = self.__GetCover__(newbookname, newcontentname, content)
                dic.setdefault("cover",dst)
            self.bookinfodic.setdefault(key,dic)
        
        
    #遍历目录
    def __WalkDir__(self):
        extes = ('.txt','.jpg')
        self.bookinfos = BaseFile.WalkDir(self.path, extes)
        for element in self.bookinfos:
            type,content,title = self.__SplitDir__(element);
            self.__AddBookInfo__(BaseUtil.GetMD5(title), title,element,type)

        #print self.bookinfodic
        
    
    