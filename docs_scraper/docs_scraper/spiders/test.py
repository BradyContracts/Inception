import scrapy
from scrapy_splash import SplashRequest

class DocsSpider(scrapy.Spider):
    name = 'docs_spider'
    start_urls = ['https://docs.python.org/3/tutorial/introduction.html']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 2})  # Use SplashRequest for JS rendering

    def parse(self, response):
        # Extract content, for example, the tutorial headings
        headings = response.xpath('//h1/text()').getall()
        for heading in headings:
            yield {'heading': heading}


def parse(self, response):
    # Print the first 500 characters of the response body to inspect it
    self.log('Response body: {}'.format(response.body[:500]))

    # Extract content
    headings = response.xpath('//h1/text()').getall()
    for heading in headings:
        yield {'heading': heading}
