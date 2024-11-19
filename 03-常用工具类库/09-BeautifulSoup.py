from bs4 import BeautifulSoup

with open('../data/poem.html', 'r', encoding='utf-8') as file:
    # 读取文件内容
    html_content = file.read()

bs = BeautifulSoup(html_content, 'html.parser')
left = bs.find(id='leftZhankai')
div_list = left.find_all('div', class_='sons')
for div in div_list:
    title = div.find('div').find_all('div')[1].find_all('p')[0].find('a').find('b').text
    author = div.find('div').find_all('div')[1].find_all('p')[1].find('a').text.replace('\n', '')
    content = div.find('div').find_all('div')[1].find('div').text[1:-1]
    print(f'{title}\n     {author[0] if len(author) > 0 else ""}\n{content}')
    # title = div.xpath('./div/div[2]/p[1]/a/b/text()')[0]
    # author = div.xpath('./div/div[2]/p[2]/a[1]/img/@alt')
    # content = '\n'.join(div.xpath('./div/div[2]/div/text()'))
