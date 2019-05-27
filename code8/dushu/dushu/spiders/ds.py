# -*- coding: utf-8 -*-
'''
1 当终端中有数据显示 但是数据没有保存 那么有可能是pipelines没有打开
2 crawlspider会给我们提供一个默认的方法结构 该方法结构使用的是return
我们一般都会返回很多的数据  但是习惯是每获得一个对象 就直接返回 所以
再for循环外使用return  那么数据返回就是for循环结束的每一个对象  这样我们
就必须要使用yield
3 当img标签中有data-original属性值的时候  我们要使用data-original而不去使用
src属性
4 无论我们获取了多少个url  那么这些url都必须要再allowed_domains的域名之下
一般我们都会书写最高路径


'''

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DsSpider(CrawlSpider):
    name = 'ds'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1179_1.html']

    rules = (
        #allow提取符合这个正则表达式的所有的连接
        Rule(LinkExtractor(allow=r'/book/1179_\d+.html'),
                           callback='parse_item',
                           follow=False),
    )

    def parse_item(self, response):
        i = {}
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #src = //div[@class="bookslist"]/ul/li//img/@src
        #alt = //div[@class="bookslist"]/ul/li//img/@alt
        #author = //div[@class="bookslist"]/ul/li/div/p[1]/text()
        li_list = response.xpath('//div[@class="bookslist"]/ul/li')
        for li in li_list:
            i['src'] = li.xpath('.//img/@data-original').extract_first()
            i['alt'] = li.xpath('.//img/@alt').extract_first()
            i['author'] = li.xpath('./div/p[1]/text()|./div/p[1]/a/text()').extract_first()
            print(i)
            yield i
