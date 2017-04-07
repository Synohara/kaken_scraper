# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KakenScraypingItem(scrapy.Item):
    # define the fields for your item here like:
    body = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    budget = scrapy.Field()
    keyword = scrapy.Field()
    keyword = scrapy.Field()
    duration = scrapy.Field()
    field = scrapy.Field()
    organization = scrapy.Field()
