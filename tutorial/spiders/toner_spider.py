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
                Rule(LinkExtractor(allow=('/toner/.*', )), callback='parse_item', follow=True),
                Rule(LinkExtractor(allow=('hq-patronen.de/(?!toner)', )) ),
            ]

    def parse_item(self, response):
        item = TonerItem()
        item['article'] = response.xpath('//div[@class='add-to-cart']/button/@data-sku/text()').extract_first()
        item['price'] = response.xpath('//b[@class='js-update-price']/text()').extract_first()
        item['url'] = response.url
        return item
