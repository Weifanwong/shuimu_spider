# -*- coding: utf-8 -*-
import pymongo
import logging 
import scrapy 
# from MongoDbHandler import MongoDbHandler
from pandas import DataFrame
import json
from qsinghua.models import *

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

conn=pymongo.MongoClient('127.0.0.1',27017)
db = conn.wwf_database01
myset = db.Shuimu_post





class QsinghuaPipeline(object):
    def process_item(self, item, spider):
    	# myset.insert('')
    	shuimu_poster = {}
    	shuimu_post = {}
    	shuimu_poster['name'] = item['poster_name']
    	shuimu_poster['sex'] = item['poster_sex']
    	shuimu_poster['post_num'] = item['poster_num']
    	shuimu_post['title'] = item['title']
    	shuimu_post['comm_num'] = item['comm_num']
    	shuimu_post['url'] = item['url']
    	shuimu_post['site_name'] = item['site_name']
    	shuimu_post['content'] = item['content']
    	shuimu_post['pt_time'] = item['pt_time']
    	shuimu_post['poster'] = shuimu_poster





    	# shuimu_poster = Poster()
    	# shuimu_poster['name'] = item['poster_name']
    	# shuimu_poster['sex'] = item['poster_sex']
    	# # shuimu_poster['post_num'] = item['poster_num']
    		
    	# shuimu_post = Post()
    	# shuimu_post['title'] = item['title']
    	# shuimu_post['comm_num'] = item['comm_num']
    	# shuimu_post['url'] = item['url']
    	# shuimu_post['site_name'] = item['site_name']
    	# shuimu_post['content'] = item['content']
    	# shuimu_post['pt_time'] = item['pt_time']
    	# shuimu_post['poster'] = shuimu_poster
    	# data = json.load(shuimu_post)
    	# print(type(data))
    	myset.insert(shuimu_post)
    	# mongoSession = MongoDbHandler('A','B', 'C')
    	return item
