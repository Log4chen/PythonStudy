from urllib import request, response,parse,robotparser,error

'''
urllib 包 包含以下几个模块：
    urllib.request - 打开和读取 URL。
    urllib.error - 包含 urllib.request 抛出的异常。
    urllib.parse - 解析 URL。
    urllib.robotparser - 解析 robots.txt 文件。
'''

request.urlopen("https://www.baidu.com")