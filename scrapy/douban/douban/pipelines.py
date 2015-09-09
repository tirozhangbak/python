# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json  
import codecs  

class DoubanPipeline(object):
    def __init__(self):  
        pass

    def process_item(self, item, spider):
        self.file = codecs.open('douban_data_utf8.json', 'awb', encoding='utf-8')
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode("unicode_escape")) 
        return item
