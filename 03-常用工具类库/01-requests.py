import requests, re

api_getUserInfo = "https://console-mock.apipost.cn/mock/49a4aff6-d34f-4327-829b-690cc21c77b7/getUserInfo?apipost_id=ba5884"

# 发送请求
x = requests.get('https://www.runoob.com/', {'user': 'tony'})
# 返回网页内容
# print(x.text)

res = requests.post(api_getUserInfo, {'userId': '123'})
print(f'status: {res.status_code} encoding: {res.encoding}') # 200 utf-8
print(res.content) # <class 'bytes'>
print(res.text) # str 类型
print(res.json()) # dict类型

# 上传文件
files = {'file': open('01-requests.py', 'rb')}
requests.post('https://httpbin.org', files=files)

res = requests.request(method='post', url=api_getUserInfo, data={'userId': '123'})