# -*- coding: utf-8 -*-
import scrapy

class LgSpider(scrapy.Spider):
    name = 'lg'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print('jintianshizhousanhaiyouliangtianpachongjieshuleshujujiayou')
