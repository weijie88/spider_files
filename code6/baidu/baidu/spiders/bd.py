# -*- coding: utf-8 -*-
import scrapy


class BdSpider(scrapy.Spider):
    #爬虫文件的名字  什么时候使用呢？  运行爬虫文件的时候需要使用name
    name = 'bd'
    #允许爬取的域名列表
    allowed_domains = ['www.baidu.com']
    #起始的url
    start_urls = ['http://www.baidu.com/']
    #该方法返回得类型一定是一个迭代得对象
    def parse(self, response):
        print('zheshiwodediyigescrapyproject nijiu bie shui')
