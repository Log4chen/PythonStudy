import requests

api_getUserInfo = "https://console-mock.apipost.cn/mock/49a4aff6-d34f-4327-829b-690cc21c77b7/getUserInfo?apipost_id=ba5884"

# 发送请求
x = requests.get('https://www.runoob.com/')
# 返回网页内容
print(x.text)

res = requests.post(api_getUserInfo)
print(f'status: {res.status_code} encoding: {res.encoding}') # 200 utf-8
print(res.content) # <class 'bytes'>
print(res.text) # str 类型
print(res.json()) # dict类型