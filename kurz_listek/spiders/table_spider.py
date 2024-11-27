import scrapy

class TableSpider(scrapy.Spider):
    name = "table_spider"  # This is the name of the spider
    start_urls = ["https://www.rb.cz/informacni-servis/kurzovni-listek"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, meta={"playwright": True})

    def parse(self, response):
        rows = response.xpath("//table//tr")
        for row in rows:
            cells = row.xpath(".//td/text()").getall()
            #if(len(cells)>0):              
                #cells = [cells[0].strip(), cells[1].strip(), cells[-1].strip()]
            if cells:
                yield {"row": cells}