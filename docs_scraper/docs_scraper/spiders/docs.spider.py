import scrapy
from scrapy_splash import SplashRequest

class DocsSpider(scrapy.Spider):
    name = 'docs_spider'
    start_urls = ['https://docs.python.org/3/tutorial/introduction.html']

    def start_requests(self):
        # Iterate through the start_urls and use SplashRequest to render the page
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 3})  # Increased wait time for rendering JS

    def parse(self, response):
        # Log the first 500 characters of the response body to inspect what is being returned
        self.log('Response body: {}'.format(response.body[:500]))

        # Extract headings (e.g., <h1> tags)
        headings = response.xpath('//h1//text()').getall()

        # Extract paragraphs (e.g., <p> tags)
        paragraphs = response.xpath('//p//text()').getall()

        # Yield the extracted data
        for heading in headings:
            yield {'heading': heading}

        for paragraph in paragraphs:
            yield {'paragraph': paragraph}
