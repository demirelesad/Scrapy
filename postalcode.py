import scrapy


class PostalcodeSpider(scrapy.Spider):
    name = 'postalcode'
    allowed_domains = ['www.postakoduturkiye.com']
    start_urls = ['https://www.postakoduturkiye.com/']

    def parse(self, response):
        for i in response.xpath('//table[@class="table table-hover table-bordered"]/tbody/tr/td[1]'):
            yield scrapy.Request(url = "https://www.postakoduturkiye.com/" + i.xpath('.//a/@href').get())
            
            yield {
                'link' : i.xpath('.//a/@href').get()
            }
