import scrapy


class WebScraperSpider(scrapy.Spider):
    name = "web-scraper"
    allowed_domains = ["www.scrapethissite.com"]
    start_urls = ["https://www.scrapethissite.com/pages/simple/"]

    def parse(self, response):
        
        country_infos = response.css('div.col-md-4.country')
        for each_country_info in country_infos:
             
            yield {
                'country_name': ' '.join(each_country_info.css('h3.country-name::text').extract()[1].split()),
                'country_capital':each_country_info.css('span.country-capital::text').get(),
                'country_population':each_country_info.css('span.country-population::text').get(),
                'country_area':each_country_info.css('span.country-area::text').get()
            }

       