# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MovieItem
#为什么要先修改为CrawlSpider  因为当前网站中得数据有很多页  所以我们得直观反映是提取连接
#所以才会想修改为CrawlSpider

class MmSpider(CrawlSpider):
    name = 'mm'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/index.html']

    rules = (
        #list_23_3.html
        Rule(LinkExtractor(allow=r'list_23_\d+.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        a_list = response.xpath('//div[@class="co_content8"]//table//tr[2]/td[2]/b/a[last()]')
        for a in a_list:
            alt = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            url = 'http://www.dytt8.net' + href
            print(url)
            movie = MovieItem(name=alt)
            yield scrapy.Request(url=url,callback=self.parse_detail,meta={'movie':movie})
    def parse_detail(self, response):
        movie = response.meta['movie']
        #//div[@id="Zoom"]//img[1]/@src'
        src = response.xpath('//div[@id="Zoom"]//img[1]/@src').extract_first()
        movie['src'] = src
        yield movie