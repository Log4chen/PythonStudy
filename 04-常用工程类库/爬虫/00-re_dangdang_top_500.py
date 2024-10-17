import requests
import re
import json

'''
使用正则表达式解析html
'''
def parse_result(html):
    pattern = re.compile(flags=re.S, pattern='<li.*?list_num.*?(\d+)\.</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span class="price_n">(.*?)</span>.*?</li>')
    items = re.findall(pattern, html)  # <class 'list'>

    for item in items:  # item 类型 <class 'tuple'>
        yield {
            'range': item[0],
            'image': item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price': item[6]
        }


def request_dandan(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException as e:
        print(e)
        return None


def write_item_to_file(item):
    print('开始写入数据 ====> ' + str(item))
    with open('../../data/dangdang_top500.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')


def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html = request_dandan(url)
    items = parse_result(html)  # items类型 <class 'generator'>
    for item in items:
        write_item_to_file(item)  # item类型 <class 'dict'>


if __name__ == "__main__":
    for i in range(1, 26):
        main(i)
