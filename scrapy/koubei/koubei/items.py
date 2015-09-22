# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KoubeiItem(scrapy.Item):
    # define the fields for your item here like:
    cate = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    weight = scrapy.Field()
    pr = scrapy.Field()
