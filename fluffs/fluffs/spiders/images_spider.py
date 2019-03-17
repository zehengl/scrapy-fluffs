import os
from urllib.parse import urlparse

import scrapy
from fluffs.items import FluffsItem


class ImagesSpider(scrapy.Spider):
    name = "images"
    start_urls = ["http://majorclanger.co.uk/fluffimagesf.htm"]

    def parse(self, response):
        urls = response.xpath("//td/img/@src").extract()
        items = [FluffsItem(image_urls=[url], name=self.get_name(url)) for url in urls]
        yield from items

    def get_name(self, url):
        """Get filename from url

        Args:
            url (str): The url

        Returns:
            str: The filename
        """

        return os.path.basename(urlparse(url).path)
