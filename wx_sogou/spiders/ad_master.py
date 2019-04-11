# -*- coding: utf-8 -*-
from urllib.parse import unquote
import os
import scrapy
from lxml import etree
from wx_sogou.items import WxSogouItem
from wx_sogou.basic_config import cookies1, cookies2
from wx_sogou.utils import gen_url, stringToDict
import random

q_type = 2  # q_type=1 搜公号，=2 搜文章
ad_owner = "洛基英语"

class AdMasterSpider(scrapy.Spider):
    name = 'ad_master'
    allowed_domains = ['weixin.sogou.com']
    # start_urls = []
    start_url_seq = []
    q_page = list(range(61, 73))
    for page_num in q_page:
        q_url = gen_url(q_type, ad_owner, page_num)
        start_url_seq.append(q_url)
        print(q_url)
    start_urls = start_url_seq
    # url_sort = list(range(len(start_url_seq)))
    # random.shuffle(url_sort)
    # for i in url_sort:
    #     start_urls.append(start_url_seq[i])
    # print(start_urls)

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, cookies=stringToDict(cookies2))  # 这里带着cookie发出请求

    def parse(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        ad_owner = response.url.split("query=")[1].split("&")[0]
        page_num = response.url.split("page=")[1].split("&")[0]
        filename = unquote(ad_owner) + "_" + page_num + ".html"
        self.logger.info('Filename is %s', filename)

        with open(os.path.join(os.getcwd(), "html", filename), "w+") as f:
            response_rm_highlight = response.body.decode("utf-8").replace("<em><!--red_beg-->", "").replace(
                "<!--red_end--></em>", "")
            f.write(response_rm_highlight)

        response = etree.parse(os.path.join("html", filename), etree.HTMLParser())
        # pdb.set_trace()
        wx_sogou_item = WxSogouItem()
        wx_sogou_item['wx_account_name'] = response.xpath("//*[@class='account']/text()")
        wx_sogou_item['wx_ad_title'] = response.xpath("//*[contains(@uigs,'article_title')]/text()")
        wx_sogou_item['wx_ad_date'] = response.xpath("//span[@class='s2']/script/text()")
        wx_sogou_item['wx_account_link'] = response.xpath("//*[@class='account']/@href")
        wx_sogou_item['wx_ad_link'] = response.xpath("//*[contains(@uigs,'article_title')]/@href")
        wx_sogou_item["page_tag"] = unquote(ad_owner) + "_" + page_num

        yield wx_sogou_item
