# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.



import scrapy
import urlparse
from tutorial.items import DmozItem



class DmozSpider(scrapy.Spider):

    name = 'dmoz'
    start_urls = ['http://www.freebuf.com/']

    def parse(self, response):
        link = response.xpath('//div[@class="news-info"]/dl/dt/a/@href').extract()
        for curUrl in link:
            curUrl = urlparse.urljoin(response.url, curUrl)
            yield scrapy.Request(url=curUrl, callback=self.parse_artiinfo)

        next_url = response.xpath('//div[@class="news-more"]/a/@href').extract()[0]

        if next_url:
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"+response.url
            print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"+next_url
            next_url = urlparse.urljoin(response.url, next_url)
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_artiinfo(self, response):
        item = DmozItem()
        item['address'] = response.url.encode('UTF-8')
        item['title'] = ''.join([''.join(x.xpath('text()').extract()) for x in response.xpath('//div[@class="articlecontent"]//div[@class="title"]/h2')])
        item['body'] = ''.join([''.join(x.xpath('text()').extract()) for x in response.xpath('//div[@class="articlecontent"]//p')])
        yield item
