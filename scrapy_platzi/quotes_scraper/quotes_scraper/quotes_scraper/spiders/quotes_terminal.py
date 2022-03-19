import scrapy

#titulo_web = //h1/a/text().get()
#citas_web = //span[@class="text" and @itemprop="text"]/text().getall() 
#top_ten_tags = //div[contains(@class,"tags-box")]//span[@class="tag-item"]/a/text()').getall()


#class QuotesSpider(scrapy.Spider):
#    name = 'quotes'
#    start_urls = [
#    'http://quotes.toscrape.com/page/1/'
#    ]

#    def parse(self, response):
#        title = response.xpath('//h1/a/text()').get()
#        print(f'Titulo: {title}')
#        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
#        print('Citas: ')
#        for quote in quotes:
#            print(f'- {quote}')
#        print('Top ten tags: ')
#        top_ten_tags = response.xpath('//div[contains(@class,"tags-box")]//span[@class="tag-item"]/a/text()').getall()
#        for tag in top_ten_tags:
#            print(f'- {tag}')
        #print(response.status,response.headers)

        