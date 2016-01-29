# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class LaracastsItem(Item):
	title = Field()
	downlink = Field()
	description = Field()
	path = Field()