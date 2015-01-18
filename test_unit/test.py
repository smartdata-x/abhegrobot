#!/usr/bin/python 
# -*- coding: utf-8 -*-  
#encoding=utf-8

'''
Created on 2015年1月13日

@author: mac
'''

from book.collection_book import CollectionBook
from pub.config  import  SingletonConfig
import os

def TestIncludedBook():
    path = "/Users/mac/Downloads/book"
    dst ="/tmp/mac/Downloads/dst/book"
    book_collection = CollectionBook(SingletonConfig().booksrc,SingletonConfig().bookdst)
    book_collection.Start()

if __name__ == '__main__':
    TestIncludedBook()
    