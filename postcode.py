import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PostcodeSpider(CrawlSpider):
    name = 'postcode'
    allowed_domains = ['www.postakoduturkiye.com']
    start_urls = ['http://www.postakoduturkiye.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//table[@class="table table-hover table-bordered"]/tbody/tr/td[1]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for i in response.xpath('//table[@class="table table-hover table-bordered"]/tbody/tr'):
            yield {
                'city' : response.url,
                'district' : i.xpath('.//td[1]/a/text()').get(),
                'postal_code' : i.xpath('.//td[2]/text()').get()
            }



