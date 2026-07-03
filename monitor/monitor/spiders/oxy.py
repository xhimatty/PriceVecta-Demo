import scrapy
import json
from datetime import datetime, timezone
from monitor.items import MonitorItem
from extraction import extract_clean_item


class OxySpider(scrapy.Spider):
    name = "oxy"
    allowed_domains = ["sandbox.oxylabs.io"]
    start_urls = [
        'https://sandbox.oxylabs.io/products/3',
        'https://sandbox.oxylabs.io/products/9',
        'https://sandbox.oxylabs.io/products/29',
    ]

    def parse(self, response):
        extracted_data = extract_clean_item(response.text)
        
        if not extracted_data:
            self.logger.error(f"Failed to extract data from {response.url}")
            return
        
        item = MonitorItem()
        
        item['store'] = 'OxyLabs'
        item['brand'] = extracted_data['brand']
        item['product'] = extracted_data['product']
        item['price'] = extracted_data['price']
        item['url'] = response.url
        item['scraped_at'] = datetime.now(timezone.utc)

        yield item
