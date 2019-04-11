# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pdb
from pandas import DataFrame
import os, time


class WxSogouPipeline(object):
    def process_item(self, item, spider):
        filepath = os.path.join(os.getcwd(), "results", item["page_tag"].split("_")[0] + ".csv")
        columns = ["wx_account_name", "wx_ad_title", "wx_ad_date", "wx_account_link", "wx_ad_link", "page_tag"]
        item_df = DataFrame(columns=columns)

        ad_dates = []
        for ad_date in item["wx_ad_date"]:
            time_value = int(ad_date.split("'")[1])
            ad_date = time.strftime("%Y-%m-%d", time.localtime(time_value))
            ad_dates.append(ad_date)
        item_df["wx_ad_date"] = ad_dates
        columns.pop(2)
        for k in columns:
            item_df[k] = item[k]

        item_df.to_csv(filepath, mode="a", header=False)
