# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DushuPipeline(object):
    def open_spider(self,spider):
        self.fp = open('dushu.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        str1 = json.dumps(item,ensure_ascii=False)
        self.fp.write(str1)
        return item

    def close_spider(self,spider):
        self.fp.close()

#1 我们再settings文件中定义了参数  那么settings中的参数如何与pipelines
#建立关联
from scrapy.utils.project import get_project_settings
import pymysql

class MysqlPipeline(object):
    #获得settings文件的连接参数
    def __init__(self):
        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.pwd = settings['DB_PASSWORD']
        self.name = settings['DB_DATABASE']
        self.charset = settings['DB_CHARSET']
        self.connect()
    #连接数据库
    def connect(self):
        self.conn = pymysql.connect(host=self.host,
                                    port=self.port,
                                    user=self.user,
                                    password=self.pwd,
                                    db=self.name,
                                    charset=self.charset)
        self.cursor = self.conn.cursor()

    #操作数据库
    def process_item(self, item, spider):
        sql = 'insert into book3(src, alt, author) values("%s", "%s", "%s")' % (
        item['src'], item['alt'], item['author'])
        # 执行sql语句
        self.cursor.execute(sql)
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()
        self.cursor.close()




