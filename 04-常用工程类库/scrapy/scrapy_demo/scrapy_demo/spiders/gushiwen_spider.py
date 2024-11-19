import scrapy

from ..items import Poem


class gushiwen_spider(scrapy.Spider):
    # 这里定义一个唯一的名称，用来标识古诗文的爬虫，在项目中不能和别的爬虫名称一样，等会会用到这个名称
    name = 'gushiwen'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }

    def start_requests(self):
        urls = [
            'https://www.gushiwen.cn/shiwens/default.aspx?page=1',
            # 'https://www.gushiwen.cn/shiwens/default.aspx?page=2'
        ]
        for url in urls:
            # 如果不指定headers，则会使用settings.py中提供的默认header
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        # page = response.url.split('=')[1]
        # filename = 'gushiwen-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        div_list = response.xpath('//*[@id="leftZhankai"]/div[@class="sons"]')
        for div in div_list:
            # yield {
            #     'title': div.xpath('./div/div[2]/p[1]/a/b/text()').get(),
            #     'author': div.xpath('./div/div[2]/p[2]/a[1]/img/@alt').get(),
            #     'dynasty': div.xpath('./div/div[2]/p[2]/a[2]/text()').get()[1:-1],
            #     'content': '\n'.join(div.xpath('./div/div[2]/div/text()').getall())[1:-1]
            # }
            item = Poem()
            # item.title = xxx 会报错，因为Poem继承自scrapy.Item，其本质是Dict字典
            item['title'] = div.xpath('./div/div[2]/p[1]/a/b/text()').get()
            item['author'] = div.xpath('./div/div[2]/p[2]/a[1]/img/@alt').get()
            item['dynasty'] = div.xpath('./div/div[2]/p[2]/a[2]/text()').get()[1:-1]
            if len(div.xpath('./div/div[2]/div/p')) == 0:
                item['content'] = '\n'.join(div.xpath('./div/div[2]/div/text()').getall())[1:-1]
            else:
                item['content'] = '\n'.join(div.xpath('./div/div[2]/div/p/text()').getall())[1:-1]
            yield item
        next_page = response.xpath('//a[@class="amore"]/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
