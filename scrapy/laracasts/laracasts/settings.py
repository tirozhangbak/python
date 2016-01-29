# Scrapy settings for laracasts project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'laracasts'
BOT_VERSION = '1.0'

ITEM_PIPELINES = ['laracasts.pipelines.LaracastsPipeline']
SPIDER_MODULES = ['laracasts.spiders']
NEWSPIDER_MODULE = 'laracasts.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
DOWNLOAD_DELAY = 1
