# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from movie.items import MovieItem
'''
分布式爬虫步骤:
    spider文件
    1 继承RedisCrawlSpider类
    2 导入RedisCrawlSpider类
    3 定义redis_key
    4 定义提取连接路径
    settings.py
    5 开启redis管道
    6 设置延迟
    7 去重组件
    8 调用器组件
    9 暂停
运行步骤：
   1 修改redis连接得host
   2 scrapy runspider fenbushi.py
   3 等我
   
          


'''

class FenbushiSpider(RedisCrawlSpider):
    name = 'fenbushi'
    allowed_domains = ['www.dytt8.net']
    # start_urls = ['http://www.dytt8.net/html/gndy/dyzz/index.html']
    #redis_key得值就是lpush得key
    #lpush fen:start_urls http://www.dytt8.net/html/gndy/dyzz/index.html
    redis_key = 'fen:start_urls'


    rules = (
        Rule(LinkExtractor(allow=r'list_23_\d+.html'),
                           callback='parse_item',
                           follow=True),
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
