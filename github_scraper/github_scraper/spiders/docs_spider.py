import scrapy
from scrapy_splash import SplashRequest

class DocsSpider(scrapy.Spider):
    name = "docs_spider"
    allowed_domains = ["docs.python.org", "numpy.org", "pytorch.org"]
    start_urls = [
        "https://docs.python.org/3/tutorial/index.html",
        "https://numpy.org/doc/stable/user/quickstart.html",
        "https://pytorch.org/docs/stable/index.html"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 2})

    def parse(self, response):
        """Extract all links from the documentation and follow them"""
        for link in response.css("a::attr(href)").getall():
            if link.startswith("http") and self.allowed_domains[0] in link:
                yield SplashRequest(link, self.parse_docs, args={'wait': 2})

    def parse_docs(self, response):
        """Extract code blocks from documentation pages"""
        for code in response.css("div.highlight pre::text").getall():  # Adjust selector for code blocks
            yield {
                "url": response.url,
                "code": code.strip()
            }


