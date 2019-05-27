# -*- coding: utf-8 -*-
import scrapy
from ..items import MovieItem
#items的属性包含了2个页面中的数据
#//div[@class="co_content8"]//table/tbody/tr[2]/td[2]/b/a[last()]/text()

class MvSpider(scrapy.Spider):
    name = 'mv'
    #http://www.dytt8.net/html/gndy/dyzz/20180909/57422.html
    #http://www.dytt8.net/html/gndy/dyzz/index.html
    allowed_domains = ['www.dytt8.net']
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/index.html']

    def parse(self, response):
        a_list = response.xpath('//div[@class="co_content8"]//table//tr[2]/td[2]/b/a[last()]')
        for a in a_list:
            alt = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            url = 'http://www.dytt8.net' + href
            print(url)
            #需要关注---对象的属性有2个 而我们传一个的时候会不会报错
            movie = MovieItem(name = alt)
            # movie = MovieItem()
            # movie['name']=alt
            #当我们写到这的时候  发现缺少第二页的数据  那么问题就是第二页的数据怎么存放到movie中
            #如果发送请求到第二页
            #当我们获取到第二页的请求的时候 那么我们需要发送这个请求给服务器 然后获取响应数据
            #对该数据进行xpath解析  获取图片的路径  然后把图片的路径保存到movie对象中
            yield scrapy.Request(url=url,callback=self.parse_detail,meta={'movie':movie})
    def parse_detail(self, response):
        movie = response.meta['movie']
        #//div[@id="Zoom"]//img[1]/@src'
        src = response.xpath('//div[@id="Zoom"]//img[1]/@src').extract_first()
        movie['src'] = src
        yield movie




