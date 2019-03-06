# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class ElectronicsSpider(CrawlSpider):
'''To use multiple crawlers on site'''

name = "mobiles"
    allowed_domains = ["www.olx.in"]
    start_urls = [
                  'https://www.olx.in/mobile-phones/',
                  'https://www.olx.in/tablets/',
                  'https://www.olx.in/accessories/'
                  ]
        
                  rules = (
                           Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
                                callback="parse_item",
                                follow=True),)
                  
                  def parse_item(self, response):
                      print('Processing..' + response.url)
