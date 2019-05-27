# -*- coding: utf-8 -*-
import scrapy


class ZzSpider(scrapy.Spider):
    name = 'zz'
    allowed_domains = ['http://sc.chinaz.com/tupian/chiqiangdongzuotupian.html']
    start_urls = ['http://sc.chinaz.com/tupian/chiqiangdongzuotupian.html']

    def parse(self, response):
        #获取响应的页面
        # text = response.text
        # print(text)
        #响应的是二进制文件
        # body = response.body
        # print(body)
        #response.xpath方法返回的数据类型是selector对象的列表

        # alt_list = response.xpath('//div[@id="container"]/div/p/a/@alt')
        # # print(alt_list)
        # for alt in alt_list:
        #     #extract()方法使用来提取selector对象的数据
        #     alt = alt.extract()
        # //div[@id="container"]/div/div/a/@src
        # //div[@id="container"]/div/div/a/@alt
        src_list = response.xpath('//div[@id="container"]/div/div//img/@src2')
        alt_list = response.xpath('//div[@id="container"]/div/div//img/@alt')
        items = []
        if len(src_list) == len(alt_list):
            for i in range(len(src_list)):
                item = {}
                src = src_list[i].extract()
                alt = alt_list[i].extract()
                item['src'] = src
                item['alt'] = alt
                items.append(item)
        return items


