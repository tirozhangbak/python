# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import MySQLdb

class LaracastsPipeline(object):
	def __init__(self):
		self.conn = MySQLdb.connect(
			user = '[数据库用户名]', 
			passwd = '[数据库密码]', 
			db = 'scrapy',
			host = '127.0.0.1',
			charset = "utf8", 
			use_unicode=True)
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):
		print('==item===================================')
		try:
			# post_id
			self.cursor.execute('insert into laracasts_lessons (id, title, downlink, description, path) values (null, %s, %s, %s, %s)', (item['title'], item['downlink'], item['description'], item['path']))
			self.conn.commit()
		except MySQLdb.Error as e:
			print "Error %d: %s" % (e.args[0], e.args[1])
		return item
