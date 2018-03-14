import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tutorial.items import TonerItem



class TonerSpider(CrawlSpider):
    name = "toner"
    allowed_domains = ['hq-patronen.de']
    start_urls = [
                    "https://www.hq-patronen.de/p/original-xerox-108r00713-bildtrommel",

                ]
    rules = [
                Rule(LinkExtractor(allow=('/p/.*', )), callback='parse_item', follow=True),
                Rule(LinkExtractor(allow=('hq-patronen.de/(?!p)', )) ),
            ]

    def parse_item(self, response):
        item = TonerItem()
        item['article'] = response.xpath('//button/@data-sku').extract_first()
        item['price'] = response.xpath('//span[@class="amount"]/text()').extract_first()
        item['url'] = response.url
        return item
