# -*- coding: utf-8 -*-
import scrapy


class BdSpider(scrapy.Spider):
    name = 'bd'
    allowed_domains = ['https://fanyi.baidu.com']
    #start_urls是一个不完整的路径  因为缺少参数
    #参数怎么添加才能是路径正确
    # start_urls = ['https://fanyi.baidu.com/sug/']
    #
    # def parse(self, response):
    #     pass
    '''
    scrapy的post请求不可以直接使用starts_urls的，因为此时的起始url并不是
    一个完整的路径 因为缺少参数  
    所以执行post请求的步骤是
    1 重写start_requests方法
    2 scrapy。FormRequest(url,callback,formdata)
                             
    '''
    def start_requests(self):
        post_url = 'https://fanyi.baidu.com/sug/'
        data = {
            'kw':'love',
        }
        yield scrapy.FormRequest(url=post_url,
                                 formdata=data,
                                 callback=self.parse_detail)
    def parse_detail(self,response):
        print(response.text)
