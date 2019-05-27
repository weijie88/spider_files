# -*- coding: utf-8 -*-
'''
alt = //div[@class="item masonry_brick masonry-brick"]/div/div/a/img/@alt
src = //div[@class="item masonry_brick masonry-brick"]/div/div/a/img/@src
price = //div[@class="item masonry_brick masonry-brick"]/div/div[@class="img"]/span
注 当做页面解析的时候  我们可以使用xpath解析出来数据 但是使用scrapy shell的时候 就没有获取
数据  那么我们需要观察页面的源代码  观察解析路径
alt = //div[@class="item masonry_brick"]/div/div/a/img/@alt
src = //div[@class="item masonry_brick"]/div/div/a/img/@src
price = //div[@class="item masonry_brick"]/div/div[@class="img"]/span
'''
import scrapy
from xiaohua.items import XiaohuaItem

class XhSpider(scrapy.Spider):
    name = 'xh'
    page = 0
    url = 'http://www.xiaohuar.com/list-1-'
    allowed_domains = ['http://www.xiaohuar.com/hua/']
    start_urls = ['http://www.xiaohuar.com/hua//']

    def parse(self, response):
        # alt = response.xpath('//div[@class="item masonry_brick"]/div/div[@class="img"]/a/img/@alt')
        # src = response.xpath('//div[@class="item masonry_brick"]/div/div[@class="img"]/a/img/@src')
        # price = response.xpath('//div[@class="item masonry_brick"]/div/div[@class="img"]/span')
        div_list = response.xpath('//div[@class="item masonry_brick"]/div/div[@class="img"]')
        for div in div_list:
            #div是一个seletor对象 然后seletor对象可以调用xpath方法进一步提取
            #扩展：response的xpath方法的返回值类型是一个seletor的列表  所以遍历xpath方法的返回值
            #那么遍历出来的每一个对象就是一个seletor对象
            #注意：如果是直接子标签也就是一个/的时候 那么我们使用的是./
            #如果是//的情况下我们使用.//
            #.代表的是当前路径
            alt = div.xpath('./a/img/@alt').extract_first()
            src = div.xpath('./a/img/@src').extract_first()
            if src.startswith('https'):
                src = src
            else:
                #发现不带https的路径和带https的路径有很大的区别
                #所以要观察不带https的路径
                src = 'http://www.xiaohuar.com' + src
            price = div.xpath('./span').extract_first()
            #如果我们使用的是建立一个列表然后列表里面放的是字典
            # item = {}
            # item['alt'] = alt
            # item['src'] = src
            # item['price'] = price
            #使用创建对象的方式比较好
            #  数据结构不容易被破坏
            item = XiaohuaItem(alt=alt,src=src,price=price)
            yield item
            #http://www.xiaohuar.com/list-1-0.html   1
            #http://www.xiaohuar.com/list-1-1.html   2
            #http://www.xiaohuar.com/list-1-2.html   3
            self.page += 1
            if self.page < 44:
                url = self.url + str(self.page) + '.html'
                #url是发送请求的资源路径  callback是回调函数  没有圆括号
                yield scrapy.Request(url=url,callback=self.parse)






