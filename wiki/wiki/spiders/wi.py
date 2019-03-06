# -*- coding: utf-8 -*-
import scrapy
import logging
logging.getLogger('scrapy').setLevel(logging.WARNING)
print("2")
class WiSpider(scrapy.Spider):
    name = 'wi'
    start_urls = ['http://www.wikipedia.org/wiki/Electric_battery/']
    print("1")
    def parse(self, response):
        pass(response.css('h1#firstHeading::text').extract())
