import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import TakeFirst, MapCompose

def format_desc(value):
    data = list(value.split('",'))
    prod_desc = list()
    for i in range(len(data)):
        if data[i] != " ":
            prod_desc.append(data[i].strip())
    return prod_desc

def format_price(value):
    price = int(value.split(' ')[1])
    return price
    

class FaballeyIndyaItem(scrapy.Item):
    product_title = Field()
    product_description = Field(input_processor = MapCompose(format_desc))
    product_price = Field(input_processor = MapCompose(format_price))
    product_img_urls = Field()