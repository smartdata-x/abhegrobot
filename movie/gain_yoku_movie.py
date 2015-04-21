#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2015年4月1日

@author: pro
'''
from api.http_api import HttpApi
from entity.data import YouKuUnit
import json
import re
import urllib

class GainYoKuMovie(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def __gain_get_vid(self,url):
        star_pos = url.find("id_")
        end_pos = url.find(".html")
        return url[star_pos+3:end_pos]
    
    def __gain_yoku_basicinfo_(self,vid):
        #url = "http://v.youku.com/player/getPlayList/VideoIDS/XODk5MTIyNjE2/Pf/4/ctype/12/ev/1"
        url = "http://v.youku.com/player/getPlayList/VideoIDS/" + vid +"/Pf/4/ctype/12/ev/1"
        return HttpApi.SpiderRequestMethodGet(url)
        
       
    def __parser_yokujson(self,strjson):
        objs =  json.loads(strjson)
        if(not objs.has_key("data")):
            return None
        obj = objs["data"][0]
        if(obj is None):
            return None
        if(not obj.has_key("ep") or not obj.has_key("ip") ):
            return None
        return obj["ep"],obj["ip"],obj["logo"],obj["title"]
        
    def __gain_yoku_player_url(self,ep,ip,vid):
        #http://211.101.18.154/getm3u8.ashx?ip=101916841&ep=MwXSSQoXJ73Z1PjG9eJxUtP3sBc81wXCWhc%3D&vid=ODIwNjY2ODY4
        d= {'ep':str(ep)}
        #url = "http://120.26.118.139/getm3u8.ashx?ip="+str(ip)+"&ep="+str(ep)+"&vid="+str(vid)
        url = "http://120.26.118.139/getm3u8.ashx?ip="+str(ip)+"&"+urllib.urlencode(d)+"&vid="+str(vid)
        return HttpApi.SpiderRequestMethodGet(url)
          
    def unit_movie_url(self,unit):
        url = unit.get_token()
        vid =  self.__gain_get_vid(url)
        self.unit_movie_vid(vid,unit)
        
        
    def unit_movie_vid(self,vid,unit):
        ep,ip,logo,title = self.__parser_yokujson(self.__gain_yoku_basicinfo_(vid))
        if ep is None:
            return
        #获取播放地址
        play_url = self.__gain_yoku_player_url(ep, ip, vid)
        desc = "视频简介:"+title+"的视频描述稍后补充"
        unit.set_name(title)
        unit.set_logo(logo)
        unit.set_desc(desc)
        unit.set_play_url(play_url)
        