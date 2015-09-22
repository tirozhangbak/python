import re
import json


from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle

from koubei.items import *
from misc.log import *

class KouBeiSpider(CrawlSpider):
    name = "koubei"
    allowed_domains = ["mediarank.sootoo.com"]
    start_urls = [
        "http://mediarank.sootoo.com/index.php/index/brand_info/id/3",
    ]
    rules = [
        #Rule(sle(allow=("tag/[^/]+/?\?focus=book$", )), callback='parse_3',follow=True),
        Rule(sle(allow=("index/brand_info/id", )), callback='parse_3',follow=True),
    ]

    def parse_1(self, response):
        items = []
        sel = Selector(response)
        cate = sel.xpath("//div[@class='main_box']/h1/text()").extract()
        sites = sel.xpath("//div[@class='main_box']/div[@class='fg']")
        for site in sites:
            item = KoubeiItem()
            item['cate'] = cate 
            item['name'] = site.xpath('div[2]/h3/a/text()').extract()
            item['url'] = site.xpath('div[2]/h3/span/a/text()').extract()
            item['weight'] = site.xpath('div[2]/p/span[1]/text()').extract()
            item['pr'] = site.xpath('div[2]/p/span[2]/text()').extract()
            items.append(item)
        info('parsed ' + str(response))
        return items

    def parse_3(self, response):
        items = []
        sel = Selector(response)
        cate = sel.xpath("//div[@class='main_box']/h1/text()").extract()
        sites = sel.xpath("//div[@class='main_box']/div[@class='fg']")
        for site in sites:
            item = KoubeiItem()
            item['cate'] = cate 
            item['name'] = site.xpath('div[2]/h3/a/text()').extract()
            item['url'] = site.xpath('div[2]/h3/span/a/text()').extract()
            item['weight'] = site.xpath('div[2]/p/span[1]/text()').extract()
            item['pr'] = site.xpath('div[2]/p/span[2]/text()').extract()
            items.append(item)
        info('parsed ' + str(response))
        return items

    def _process_request(self, request):
        info('process ' + str(request))
        return request
