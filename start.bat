if exist output.json del /f output.json
scrapy crawl table_spider -o output.json