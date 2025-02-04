from lxml import etree
'''
可以通过在浏览器安装xpath helper之类的插件，快速获取xpath表达式
'''
tree = etree.parse('../data/poem.html', etree.HTMLParser())
div_list = tree.xpath('//*[@id="leftZhankai"]/div[@class="sons"]')
for div in div_list:
    title = div.xpath('./div/div[2]/p[1]/a/b/text()')[0]
    author = div.xpath('./div/div[2]/p[2]/a[1]/img/@alt')
    content = '\n'.join(div.xpath('./div/div[2]/div/text()'))

    print(f'{title}\n     {author[0] if len(author) > 0 else ""}\n{content}')