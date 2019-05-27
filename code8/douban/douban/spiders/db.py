# # -*- coding: utf-8 -*-
# import scrapy
#
# '''
# 概要分析：登陆之后进入个人主页
#
# 需求分析：
#         1 登陆：有时候有验证码  有时候没有验证码
#
# 先到登陆的页面     get
# 如果有验证码  那就下载验证码   没有验证码  直接登陆   post
# 进入到个人主页     get
#
# get - post -get
#
# 难点：登陆页面的接口和登陆的接口一样
# 登陆页面的接口：https://www.douban.com/accounts/login
# 登陆的接口指的是 提交表单接口：https://www.douban.com/accounts/login
#
# '''
# import urllib.request
#
# class DbSpider(scrapy.Spider):
#     name = 'db'
#     allowed_domains = ['www.douban.com']
#     start_urls = ['https://www.douban.com/accounts/login']
#
#     def parse(self, response):
#         #当我们再终端中执行scrapy crawl db的时候 就会执行start_urls
#         #response中就是响应的数据
#         img_url = response.xpath('//img[@id="验证码id"]/@src').extract_first()
#         if not img_url:
#             data={
#                 'name':'18642820892',
#                 'pwd':'1234'
#                 #这个网站设计的是  没有验证码的时候也没有隐藏域
#             }
#         else:
#             urllib.request.urlretrieve(url=img_url,filename='a.jpg')
#             yanzhengma = input('请输入验证码')
#             ycy = response.xpath('yincangyuxpath路径').extract_first()
#             data={
#                 'name': '18642820892',
#                 'pwd': '1234',
#                 '隐藏于':ycy,
#                 'yzm':yanzhengma
#             }
#             #这个是点击登陆的请求（这个请求和跳转到登陆页面的接口一样）
#             post_url = 'https://www.douban.com/accounts/login'
#             #注意：当执行了2次相同的请求的时候  有时候不会执行第二次那个一样的请求 所以
#             #我们需要添加一个属性 dont_filter = True
#             yield scrapy.FormRequest(url=post_url,formdata=data,callback=self.hehe)
#     def hehe(self,response):
#         #代表的个人主页的请求
#         get_url = 'https://www.douban.com/accounts/pro/3127387192'
#         yield scrapy.Request(url=get_url,callback=self.haha)
#     def haha(self,response):
#         with open('haha.html','w',encoding='utf-8')as fp:
#             fp.write(response.text)

#
#
#
#
#
#
#
#
#
# -*- coding: utf-8 -*-
import scrapy
import urllib.request

class DoubanSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/login']

    def parse(self, response):
        # 去查找有没有验证码
        # 【注】如果找不到，那么返回None
        image_url = response.xpath('//img[@id="captcha_image"]/@src').extract_first()
        # print('*'*50)
        # print(image_url)
        # print('*'*50)
        # exit()
        # 如果没有验证码图片，image_url就是None
        if not image_url:
            data = {
                'source': '',
                'redir': 'https://www.douban.com',
                'form_email': '595165358@qq.com',
                'form_password': 'lijing1150501',
                'login': '登录',
            }
        else:
            # 获取验证码id  隐藏于
            captcha_id = response.xpath('//input[@name="captcha-id"]/@value').extract_first()
            # 保存验证码图片，并且提示用户输入验证码
            urllib.request.urlretrieve(image_url, './douban.png')
            yanzhengma = input('请输入验证码:')
            data = {
                'source': '',
                'redir': 'https://www.douban.com',
                'form_email': '595165358@qq.com',
                'form_password': 'lijing1150501',
                'captcha-solution': yanzhengma,
                'captcha-id': captcha_id,
                'login': '登录',
            }
        post_url = 'https://accounts.douban.com/login'
        yield scrapy.FormRequest(url=post_url, formdata=data, callback=self.hehe)

    def hehe(self, response):
        # with open('douban.html', 'wb') as fp:
        #   fp.write(response.body)
        url = 'https://www.douban.com/accounts/'
        yield scrapy.Request(url=url, callback=self.dongguan)

    def dongguan(sef, response):
        with open('dong.html', 'wb') as fp:
            fp.write(response.body)
