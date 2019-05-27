# -*- coding: utf-8 -*-
import scrapy

#代理是使用中间件实现的  也就是再执行请求之前会给我们一个代理ip 然后通过这个ip
#进行访问
#步骤：
    # 1 再settings文件中开启中间件
    # 2 再开启的中间的类中定义方法  def process_request(self,request,spider)

class DlSpider(scrapy.Spider):
    name = 'dl'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/s?wd=ip']

    def parse(self, response):
        with open('daili.html','w',encoding='utf-8')as fp:
            fp.write(response.text)
