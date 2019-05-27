# -*- coding: utf-8 -*-
import scrapy


class QbSpider(scrapy.Spider):
    name = 'qb'
    allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']
    #//div[@id="content-left"]/div/div[starts-with(@class,"author")]/a/img/@alt
    #//div[@id="content-left"]/div/div[starts-with(@class,"author")]/a/img/@src
    def parse(self, response):
        items = []
        alt_list = response.xpath('//div[@id="content-left"]/div/div[starts-with(@class,"author")]/a/img/@alt')
        src_list = response.xpath('//div[@id="content-left"]/div/div[starts-with(@class,"author")]/a/img/@src')
        if len(alt_list) == len(src_list):
            for i in range(len(alt_list)):
                item = {}
                alt = alt_list[i].extract()
                src = src_list[i].extract()
                item['alt'] = alt
                item['src'] = src
                items.append(item)
        return items


