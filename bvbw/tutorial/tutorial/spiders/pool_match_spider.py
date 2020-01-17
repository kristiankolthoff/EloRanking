import scrapy
from scrapy import Selector

class PoolSpider(scrapy.Spider):
    name = "pool-match-spider"
    start_urls = ["https://bvbw.billardarea.de/cms_leagues/plan/6505/8756"]
    
    def parse(self, response):
        for href in response.xpath('//a[contains(@href,"cms_leagues/matchday")]/@href'):
            yield response.follow(href, self.parse_matches)
                                  
    
    def parse_matches(self, response):
        home_players = response.xpath('//td[contains(@class,"home up")]/text()').extract()
        away_players = response.xpath('//td[contains(@class,"visitor up")]/text()').extract()
        home_points = response.xpath('//td[contains(@class,"home down")]/text()').extract()
        away_points = response.xpath('//td[contains(@class,"visitor down")]/text()').extract()
        indexes = [0, 2, 3, 4, 5, 9, 11, 12, 13, 14]
        home_points = self.remove_indices(home_points, indexes)
        home_points = [int(home_point.strip()) for home_point in home_points]
        away_points = self.remove_indices(away_points, indexes)
        away_points = [int(away_point.strip()) for away_point in away_points]
        for home_player, away_player, home_point, away_point in zip(home_players, away_players, home_points, away_points):
        	if not (home_player == "Freilos") and not (away_player == "Freilos"):
        		yield dict(home_player=home_player, away_player=away_player, home_point=home_point, away_point=away_point)

    def remove_indices(self, list, indices):
        for index in sorted(indices, reverse=True):
    	    del list[index]
        return list
