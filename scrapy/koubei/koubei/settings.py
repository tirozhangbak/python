# -*- coding: utf-8 -*-

# Scrapy settings for koubei project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import sys 
import os

from os.path import dirname
path = dirname(dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append(path)

BOT_NAME = 'koubei'

SPIDER_MODULES = ['koubei.spiders']
NEWSPIDER_MODULE = 'koubei.spiders'

DOWNLOADER_MIDDLEWARES = { 
    'misc.middleware.CustomUserAgentMiddleware': 401,
}

ITEM_PIPELINES = { 
    'koubei.pipelines.JsonWithEncodingPipeline': 300,
}

AJAXCRAWL_ENABLED = True
   
LOG_LEVEL = 'INFO'
   

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'koubei (+http://www.yourdomain.com)'
