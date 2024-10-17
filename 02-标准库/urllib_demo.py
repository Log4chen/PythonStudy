from urllib import request, response,parse,robotparser,error

'''
urllib 包 包含以下几个模块：
    urllib.request - 打开和读取 URL。
    urllib.error - 包含 urllib.request 抛出的异常。
    urllib.parse - 解析 URL。
    urllib.robotparser - 解析 robots.txt 文件。
'''

resp = request.urlopen("https://www.baidu.com")

print(f'status: {resp.status}')
print(resp.headers)
print(resp.read().decode('utf-8'))

o = parse.urlparse("https://www.runoob.com/?s=python+%E6%95%99%E7%A8%8B")
print(o.scheme)

