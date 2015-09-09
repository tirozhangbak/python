#!/usr/bin/python
# -*- coding:utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector

from douban.items import DoubanItem 


class W3schoolSpider(Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = [
        "http://movie.douban.com/subject/26289144/"
    ]
    rules = [
        Rule(sle(allow=("/tag/[^/]+/?$", )), follow=True),        
    ]

    def parse(self, response):

        sel = Selector(response)
        #sites = sel.xpath('//div[@id="hot-comments"]/div[@class="comment-item"]/div[@class="comment"]/h3/span[2]')
        sites = sel.xpath('//div[@id="hot-comments"]/div[@*]/div[@*]/h3/span[2]')
        items = []
        movieName = sel.xpath('//div[@id="content"]/h1/span[1]/text()').extract()

        for site in sites:
            item = DoubanItem()

            userName = site.xpath('a/text()').extract()
            userScore= site.xpath('span[1]/@class').extract()

            item['movieName'] = [t.encode('utf-8') for t in movieName]
            item['userName'] = [t.encode('utf-8') for t in userName]
            item['userScore'] = [l.encode('utf-8') for l in userScore]
            items.append(item)

        return items

