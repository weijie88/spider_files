# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ZhanzhangPipeline(object):
    #item就是items中的每一个元素
    def process_item(self, item, spider):
        str1 = json.dumps(item,ensure_ascii=False)
        with open('zz.json','a',encoding='utf-8')as fp:
            fp.write(str1)
        return item
