# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaohuaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    alt = scrapy.Field()
    src = scrapy.Field()
    price = scrapy.Field()
