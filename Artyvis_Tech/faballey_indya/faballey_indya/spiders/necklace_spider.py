import scrapy
from faballey_indya.items import FaballeyIndyaItem
from scrapy.loader import ItemLoader


class NecklaceSpider(scrapy.Spider):
    name = "necklace_sets"
    start_urls = ['https://www.houseofindya.com/zyra/necklace-sets/cat']
    
    def parse(self, response):
        product_urls = response.css('ul#JsonProductList li[data-url]::attr(data-url)').getall()
        for url in product_urls:
            yield response.follow(url, callback=self.parse_item)

    def parse_item(self, response): 
        loader = ItemLoader(item=FaballeyIndyaItem(), selector=response)
        loader.add_css('product_title','div.prodRight h1::text')
        loader.add_css('product_description','div.prodRight div.prodecCntr div#tab-1 p::text')
        loader.add_css('product_price','div.prodRight h4  span:nth-of-type(2)::text')
        loader.add_css('product_img_urls','div.prodLeft ul.sliderBox a[data-image]::attr(data-image)')
        yield loader.load_item()  