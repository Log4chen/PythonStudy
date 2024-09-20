'''
os 模块：os 模块提供了许多与操作系统交互的函数，例如创建、移动和删除文件和目录，以及访问环境变量等。

sys 模块：sys 模块提供了与 Python 解释器和系统相关的功能，例如解释器的版本和路径，以及与 stdin、stdout 和 stderr 相关的信息。

time 模块：time 模块提供了处理时间的函数，例如获取当前时间、格式化日期和时间、计时等。

datetime 模块：datetime 模块提供了更高级的日期和时间处理函数，例如处理时区、计算时间差、计算日期差等。

random 模块：random 模块提供了生成随机数的函数，例如生成随机整数、浮点数、序列等。

math 模块：math 模块提供了数学函数，例如三角函数、对数函数、指数函数、常数等。

re 模块：re 模块提供了正则表达式处理函数，可以用于文本搜索、替换、分割等。

json 模块：json 模块提供了 JSON 编码和解码函数，可以将 Python 对象转换为 JSON 格式，并从 JSON 格式中解析出 Python 对象。

urllib 模块：urllib 模块提供了访问网页和处理 URL 的功能，包括下载文件、发送 POST 请求、处理 cookies 等。
'''

import json
'''
json
'''

# 字典转换为json字符串
data = {'name': 'Bob', 'age': 25, 'city': 'San Francisco'}
json_str = json.dumps(data)
print(type(json_str))

# json字符串转换为字典
json_dict = json.loads(json_str)
print(type(json_dict))
print(json_str)
print(json_dict)

# 美化输出
data = {'name': 'Bob', 'age': 25, 'city': 'San Francisco'}
json_data = json.dumps(data, indent=4, sort_keys=True)
print(json_data)

# 写入JSON文件
with open('data.json', 'w') as file:
    json.dump(data, file)

# 读取JSON文件
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
    print(loaded_data)