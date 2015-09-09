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
    allowed_domains = ["koubei.baidu.com"]
    start_urls = [
        "http://koubei.baidu.com/rank?nav=rank#13",
    ]
    rules = [
        #Rule(sle(allow=("tag/[^/]+/?\?focus=book$", )), callback='parse_3',follow=True),
    ]

    def parse(self, response):
        items = []
        sel = Selector(response)
        sites = sel.xpath('//div[@id="Pj_Rank_List"]/ul/li')
        for site in sites:
            item = KoubeiItem()
            item['title'] = site.xpath('a/div/h3/text()').extract()
            items.append(item)
            print item
        info('parsed ' + str(response))
        return items

    def _process_request(self, request):
        info('process ' + str(request))
        return request
