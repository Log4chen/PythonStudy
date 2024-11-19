import scrapy


class gushiwen_spider(scrapy.Spider):
    # 这里定义一个唯一的名称，用来标识古诗文的爬虫，在项目中不能和别的爬虫名称一样，等会会用到这个名称
    name = 'gushiwen'

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }

    def start_requests(self):
        urls = [
            # 'https://www.gushiwen.cn/shiwens/default.aspx?page=1',
            'https://www.gushiwen.cn/shiwens/default.aspx?page=2'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.header)

    def parse(self, response):
        # page = response.url.split('=')[1]
        # filename = 'gushiwen-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        left = response.xpath('//*[@id="leftZhankai"]')
        div_list = left.xpath('./div[@class="sons"]')
        for div in div_list:
            p = div.xpath('./div/div[2]/p')
            title = p[0].xpath('./a/b/text()').get()
            print(title)
            author = p[1].xpath('./a/b/text()').get()
            # print(author)

