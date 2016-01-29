from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request, FormRequest
from laracasts.items import LaracastsItem
import os,datetime,urlparse

today = datetime.date.today()

class LaracastsSpider(BaseSpider):
	name = 'laracasts'
	start_urls = ['https://laracasts.com/login']
	def parse(self, response):
		html = HtmlXPathSelector(response)
		f = html.select('//div[@id="login"]/form')
		formdata={
            'email': '[登录邮件]',
            'password': '[登录密码]',
            'remember':''
		}
		return [FormRequest.from_response(response,
			formnumber = 1,
	        formdata=formdata, headers = {
				'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.6 Safari/537.36',
	        }, callback=self.after_login)]

	def after_login(self, response):
		# if not 'xiaozi' in response.body:
		# 	print('login failed <<<>>>')
		# 	# print(response.body[1024*4:1024*8])
		# 	return None
		# print('login success <<<>>>')

		# yield Request('https://laracasts.com/lessons?page=1&format=list', callback=self.real_parse)
		for i in range(1, 11):
			yield Request('https://laracasts.com/lessons?page=' + str(i) + '&format=list', callback=self.real_parse)
	def real_parse(self, response):
		html = HtmlXPathSelector(response)
		links = html.select('//td[@class="table-title"]/a/@href').extract()
		for link in links:
			print link
			yield Request(link, callback=self.parse_page)
		'''
		for section in sections:
			top_level = section.select('.//h3/a/text()').extract()[0]
			categories = section.select('.//p[@class="pd-category"]')
			for category in categories:
				count = int(category.select('./small/text()').extract()[0][1:-1])
				if count:
					link = category.select('./a/@href').extract()[0]
					name = category.select('./a/text()').extract()[0]
					# print(name, 'http://www.laracasts.com' + link)
					yield Request('http://www.laracasts.com' + link, meta={'top_level': top_level, 'sub_level': name}, callback=self.parse_item)
		'''
	def parse_page(self, response):
		html = HtmlXPathSelector(response)
		description = html.select('//div[contains(@class, "lesson-body")]/node()').extract()[0].strip()
		titleArea = html.select('//h1[@class="lesson-title"]')
		title = titleArea.select('./text()').extract()[1].strip()
		dlink = 'https://laracasts.com' + titleArea.select('./a/@href').extract()[0]

		item = {}
		item['title'] = title.encode('utf-8')
		item['downlink'] = dlink.encode('utf-8')
		item['description'] = description.encode('utf-8')
		yield Request(item['downlink'], meta = {'itemx': item}, callback = self.save_attach)
		# return item

	def save_attach(self, response):
		attachdir = '/usr/local/laracasts/'
		itemx = response.meta['itemx']
		item = LaracastsItem()
		item['title'] = itemx['title']
		item['downlink'] = itemx['downlink']
		item['description'] = itemx['description']

		segs = urlparse.urlparse(response.url)
		thisdir = os.path.dirname(segs.path).strip('/')
		filename = os.path.basename(segs.path)
		item['path'] = os.path.join(thisdir, filename)
		thisdir = os.path.join(attachdir, thisdir)
		if not os.path.exists(thisdir):
			os.makedirs(thisdir, 777)
		dp = os.path.join(thisdir, filename)
		print dp
		open(dp, 'wb').write(response.body)
		return item
