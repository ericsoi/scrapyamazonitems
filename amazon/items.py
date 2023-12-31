# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class LaptopItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    review_count = scrapy.Field()