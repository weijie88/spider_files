# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class QiubaiPipeline(object):
    def process_item(self, item, spider):
        # str1 = json.dumps(item,ensure_ascii=False)
        # with open('qb.json','a',encoding='utf-8')as fp:
        #     fp.write(str1)
        return item
