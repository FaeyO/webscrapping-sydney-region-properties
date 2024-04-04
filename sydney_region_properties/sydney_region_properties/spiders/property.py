import scrapy


class PropertySpider(scrapy.Spider):
    name = "property"
    allowed_domains = ["www.domain.com.au"]
    start_urls = ["https://www.domain.com.au/sale/sydney-region-nsw/?excludeunderoffer=1"]


    def parse(self, response):
        houses = response.xpath("//ul[@data-testid='results']/li")
        for house in houses:
            url_1 = house.xpath(".//a[@class='css-4fwlof']/@href").get()
            if url_1 is None:
                url_1 = 'not available'
                #url_1 = house.xpath(".//div[@class='slick-slide slick-active slick-current']/div/a/@href").get()

            name = house.xpath(".//h2[@class='css-2ixxh8']/text()").get()
            location = house.xpath(".//span[@class='css-1l7mgse']/text()").get()
            link_1 = 'not_found'
            try:
                link_1 = house.xpath(".//div[@class='css-hlnxku']/a/@href").get()
            except Exception as e:
                self.logger.error(f"Error extracting link_1: {e}")
                
            if link_1 is None:
                continue
            else:
                yield scrapy.Request(url=link_1, callback=self.parse_accomodation, meta={'url_1_link':url_1,'property_name':name,'property_location':location,'property_link_1':link_1})

    def parse_accomodation(self,response):
        url_1 = response.request.meta['url_1_link']
        name = response.request.meta['property_name']
        location = response.request.meta['property_location']
        link_1 = response.request.meta['property_link_1']
        description = response.xpath("//div[@class='noscript-expander-content css-1mnayj9']/div/div/p/text()").get()
        website_link = response.xpath("//div[@class='css-13pmxen']/a/@href").get()
        contact = response.xpath("//a[@data-testid='listing-details__phone-cta-button highlight']/@href").get()

        
        yield{
            'url_1':url_1,
            'name':name,
            'location':location,
            'link_1':link_1,
            'description':description,
            'website_link':website_link,
            'contact':contact[4:]
        }


