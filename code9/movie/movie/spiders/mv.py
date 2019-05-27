# -*- coding: utf-8 -*-
import scrapy
from ..items import MovieItem


class MvSpider(scrapy.Spider):
    name = 'mv'

    allowed_domains = ['www.dytt8.net']
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/index.html']

    def parse(self, response):
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




