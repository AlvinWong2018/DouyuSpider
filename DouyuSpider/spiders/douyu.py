# -*- coding: utf-8 -*-
import scrapy
import json
from DouyuSpider.items import DouyuspiderItem

class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['www.douyu.com', 'rpic.douyucdn.cn', 'staticlive.douyucdn.cn']

    base_url = "https://www.douyu.com/api/v1/getVerticalRoom?limit=20&offset="
    offset = 0

    start_urls = [base_url + str(offset)]

    def parse(self, response):
        data_list = json.loads(response.body)["data"]

        if len(data_list) == 0:
            return

        for data in data_list:
            item = DouyuspiderItem()
            item['nickname'] = data["nickname"]
            item['imagelink'] = data["vertical_src"]
            yield item

        self.offset += 20
        yield scrapy.Request(self.base_url+str(self.offset), callback=self.parse)
