import scrapy
from scrapy import Selector

class PoolSpider(scrapy.Spider):
    name = "pool-player-spider"
    start_urls = ["https://bvbw.billardarea.de/cms_leagues/plan/6505/8756"]
    
    def parse(self, response):
        for href in response.xpath('//a[contains(@href,"playerlist")]/@href'):
            yield response.follow(href, self.parse_players)
                                  
    
    def parse_players(self, response):
        names = response.xpath('//a[contains(@href,"playerdetails")]/text()').extract()
        ids = response.xpath('//a[contains(@href,"playerdetails")]/@href').extract()
        ids = [idd.split('/')[len(idd.split('/'))-1] for idd in ids]
        clubs = response.xpath('//td[contains(@style,"text-align:left") and position() mod 2 = 1]/text()').extract()
        for name, id, club in zip(names, ids, clubs):
        	yield dict(name=name, id=id, club=club.strip())
