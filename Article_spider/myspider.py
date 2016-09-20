import scrapy

class ArticleSpider(scrapy.Spider):
    name = "article"
    start_urls = [
        'http://www.cse.zju.edu.cn/redir.php?catalog_id=131&flag=1',
    ]

    def parse(self, response):
        for article in response.css('div.c_list'):
            yield {
                'title': article.css('a::attr("title")').extract_first(),
                'date': article.xpath('span/text()').extract_first(),
                'link': 'http://www.cse.zju.edu.cn/' + article.css('a::attr("href")').extract_first()
            }

        next_page = response.css('a#page_next::attr("href")').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback = self.parse)