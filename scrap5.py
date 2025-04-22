##para ejecutar 
#scrapy runspider, primero esto
#city_trenton.py, este es el nombre del archivo
#-o pruebamera.csv, es el nombre del archivo
#-t csv, formato en que saldrá el archivo
#scrapy runspider city_trenton.py -o pruebamera.csv -t csv

from scrapy.item import Field, Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup
from scrapy.loader.processors import MapCompose

class cityUS(Item):
    city = Field()
    
    
class cityUSCrawler(CrawlSpider):
    name = "CityCrawler"
    start_urls = ['http://www.city-data.com/work/']
    allowed_domains = ['city-data.com']
    custom_settings = {
        'DOWNLOAD_DELAY': 2,
    }

    rules = (
        Rule(LinkExtractor(allow=r'-Alaska.html', restrict_xpaths='//tr[@class="col-md-6"]'), callback='parse_items'),
    )


    #//*[@id="tabs_by_category"]
    def parse_items(self, response):
        item = ItemLoader(cityUS(), response)
        item.add_xpath('city', '//*[@id="tabs_by_category"]/text()')
        item.add_xpath('Alaska', '//*[@id=tab-list tab-list-short]/text()')
        #item.add_xpath('density', '//*[@id="population-density"]/p[2]/text()[1]')
        #item.add_xpath('income', '//*[@id="median-income"]/text()')
        #item.add_xpath('cost_living', '//*[@id="cost-of-living-index"]/text()')
        #item.add_xpath('gross_rent', '//*[@id="median-rent"]/p/text()')
        #item.add_xpath('price_house_unit', '//*[@id="median-income"]/text()')
        #item.add_xpath('rate_crime', '//*[@id="crimeTab"]/tfoot/tr/td[13]')
        #item.add_xpath('zip_code', '//*[@id="zip-codes"]/p/a/text()')
       

        soup = BeautifulSoup(response.body)
        
        info_1 = soup.find(id="tabs_by_category")
        industry = info_1.text
        item.add_value('industry', industry)
        
        #info_2 = soup.find(id='hD1_0')
        #occupation = info_2.text
        #item.add_value('occupation', occupation)
        
        #info_3 = soup.find(id='schools')
        #collegue = info_3.text
        #item.add_value('collegue', collegue)
        
        #info_4 = soup.find(id='hospitals')
        #hospital = info_4.text
        #item.add_value('health_care', hospital)

        yield item.load_item()

# scrapy runspider city_trenton.py -o "Nombre del archivo.csv" -t csv --set CLOSESPIDER_ITEMCOUNT=30

# ITEM se define como una clase comun y corriente