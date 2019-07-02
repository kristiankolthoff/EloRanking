import scrapy

class PoolSpider(scrapy.Spider):
    name = "pool-spider"
    start_urls = ["https://bvbw.billardarea.de/cms_leagues/plan/5836/7925"]
    
    def parse(self, response):
        #Follow links to match pages
        for href in response.xpath('//table[@class="matchday_table"]/a/@href'):
            yield response.follow(href, self.parse_matches)
        
        #print("Pagination: ", response.css('a.next::attr(href)'))
        #Follow pagination links
        #for href in response.css('a.next::attr(href)'):
         #   yield response.follow(href, self.parse)
                                  
    
    def parse_matches(self, response):
        #name= response.xpath('//span[@itemprop="name"]/span/text()').extract_first()
        #streetAddress = response.xpath('//span[@itemprop="streetAddress"]/text()').extract_first()
        #postalCode = response.xpath('//span[@itemprop="postalCode"]/text()').extract_first()
        #latitude = response.xpath('//meta[@property="place:location:latitude"]/@content').extract_first()
        #longitude = response.xpath('//meta[@property="place:location:longitude"]/@content').extract_first()
        print(response)
        match_result = dict(name=name)
        yield match_result        
