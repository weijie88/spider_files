# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import urllib.request
class XiaohuaPipeline(object):
    #再爬虫文件开始的时候就会打开这个文件
    #以下两种方法都可以使用无论是init方法还是open_spider方法
    def open_spider(self, spider):
         # with open('xh.json','w',encoding='utf-8')as fp:
        self.fp = open('xh.json', 'w', encoding='utf-8')
    # def __init__(self):
    #     with open('xh.json', 'w', encoding='utf-8')as fp:
    #         self.fp = open('xh.json', 'w', encoding='utf-8')


    def process_item(self, item, spider):
        #item是返回列表中的每一个元素  这种写法缺点  每传过来一个对象  那么
        #就会打开一次文件 然后再文件的末尾进行追加  每个网站的数据量都会很大
        #所以文件的io操作比较频繁
        # with open('xh.json','a',encoding='utf-8')as fp:
        #     fp.write()
        #注意 直接传过来的item对象不是python对象 而是我们自定义的一个对象
        #所以不能直接序列化   如果想实现序列化 那么就需要将自定义的对象变成
        #python对象
        item1 = dict(item)
        str1 = json.dumps(item1,ensure_ascii=False)
        self.fp.write(str1)
        return item
    #再爬虫结束后就会关闭这个文件
    def close_spider(self,spider):
        self.fp.close()
#这是一个下载图片的管道
class XixiHahaPipeline(object):
    def process_item(self, item, spider):
        src = item['src']
        suffix = src.split('.')[-1]
        alt = item['alt'] + suffix
        filename = './fenger/'+alt
        urllib.request.urlretrieve(url=src,filename=filename)
        return item
