import json

# 字典转换为json字符串
data = {'name': 'Bob', 'age': 25, 'city': 'San Francisco'}
json_str = json.dumps(data)
print(type(json_str)) # str
print(json_str)

# json字符串转换为字典
json_dict = json.loads(json_str)
print(type(json_dict)) # dict
print(json_dict)

# 美化输出
data = {'name': 'Bob', 'age': 25, 'city': 'San Francisco'}
json_data = json.dumps(data, indent=4, sort_keys=True)
print(json_data)

# 写入JSON文件
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4, sort_keys=True)

# 读取JSON文件
with open('data.json', 'r') as file:
    loaded_data = json.load(file)
    print(type(loaded_data)) # dict
    print(loaded_data)


class User():
    name = None
    age = None
    city = None

    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city


# 类似JSON.toJSONString(Object)
'''
dir(obj) 返回一个包含obj大多数属性名的列表，包括方法名
getattr(obj, key): 获取obj对象中名为key的属性的值
not key.startswith('__')：确保不是私有属性或方法
not callable(getattr(obj, key)): 确保属性不是方法
'''
def object_to_dict(obj):
    return {
        key: getattr(obj, key)
        for key in dir(obj)
        if not key.startswith('__') and not callable(getattr(obj, key))
    }

user = User('tony', 20, '南京')
user_dict = object_to_dict(user)
print(user_dict)
user_str = json.dumps(user_dict, ensure_ascii=False)
print(user_str)