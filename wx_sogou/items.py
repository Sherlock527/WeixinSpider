# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class WxSogouItem(scrapy.Item):
    # define the fields for your item here like:
    wx_account_name = scrapy.Field()
    wx_ad_title = scrapy.Field()
    wx_ad_date = scrapy.Field()
    wx_account_link = scrapy.Field()
    wx_ad_link = scrapy.Field()
    page_tag = scrapy.Field()
