import scrapy
from scrapy_splash import SplashRequest

class TestSplashSpider(scrapy.Spider):
    name = 'test_splash'

    def start_requests(self):
        yield SplashRequest(
            url='http://httpbin.org/ip',
            callback=self.parse,
        )

    def parse(self, response):
        self.logger.info(f"Response: {response.text}")