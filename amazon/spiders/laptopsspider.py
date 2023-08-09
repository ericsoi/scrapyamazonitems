import scrapy
from scrapy_playwright.page import PageMethod
from amazon.items import LaptopItem

class LaptopsspiderSpider(scrapy.Spider):
    name = "laptopsspider"
    def start_requests(self):
        #Use Playwright to get javascript content from webpage
        yield scrapy.Request("https://www.amazon.com/s?k=laptops", 
                             meta=dict(
                                playwright = True,
                                playwright_include_page = True,
                                playwright_page_coroutines = [
                                    #Wait for page to load before continuing
                                    PageMethod('wait_for_selector', 'div.s-result-item')
                                ]
                             ))
    async def parse(self, response):
        laptops = response.css('div.s-result-item')
        for laptop in laptops:
            item = LaptopItem()
            #Scrap what you need
            item['title'] = laptop.css('span.a-text-normal::text').get()
            item['price'] = laptop.css('span.a-price .a-offscreen::text').get()
            item['rating'] = laptop.css('span.a-icon-alt::text').get()
            item['review_count'] = laptop.css('span.a-size-base::text').get()
            yield item
