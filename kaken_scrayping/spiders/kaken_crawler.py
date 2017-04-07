# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from kaken_scrayping.items import KakenScraypingItem 
class KakenCrawlerSpider(CrawlSpider):
    name = 'kaken_crawler'
    allowed_domains = ['kaken.nii.ac.jp']
    start_urls = ['https://kaken.nii.ac.jp/search/?kw=']

    rules = (
        Rule(LinkExtractor(allow=r'/search/'), follow=True),
        Rule(LinkExtractor(allow=r'/grant/KAKENHI'), callback='parse_item'),
    )

    def parse_item(self, response):
        i = KakenScraypingItem()
        i['body'] = response.xpath('//*[text()="Outline of Annual Research Achievements"]/following-sibling::td/p/text()').extract()
        i['title'] = response.xpath('//*[@id="listings-page"]/div[1]/div[2]/div[1]/h1/text()').extract()
        i['author'] = response.xpath('//*[@id="listings-page"]/div[1]/div[2]/div[2]/div/table/tr[6]/td/h4/span/a/text()').extract()
        i['budget'] = response.xpath('//*[text()="Budget Amount\xa0"]/following-sibling::td/text()').extract()
        i['keyword'] = response.xpath('//*[text()="Keywords"]/following-sibling::td/text()').extract()
        i['duration'] = response.xpath('//*[@id="listings-page"]/div[1]/div[2]/div[2]/div/table/tr[7]/td/span/text()').extract()
        i['field'] = response.xpath('//*[text()="Research Field"]/following-sibling::td/a[@class="link-page underline"]/text()').extract()
        i['organization'] = response.xpath('//*[text()="Research Institution"]/following-sibling::td/*[@class="link-page underline"]/text()').extract()
        yield i
