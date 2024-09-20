# 变量赋值
'''
1、Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
2、在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
3、一个变量可以通过赋值指向不同类型的对象
'''
a = 1
print(1)
a = '123'
print(a)

a = b = c = 1
a, b, c = 1, 2, "runoob"

# 数据类型
'''
Number（数字）: 
    int
    float
    bool （bool 是 int 的子类）: True、False (首字符大写)
    complex（复数）
String（字符串）
    不可变（'abc'[0] = 'e' 会报错）
    Python 没有单独的字符类型，一个字符就是长度为1的字符串
bool（布尔类型）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）-- 相当于Map

# string、list 和 tuple 都属于 sequence（序列）
'''

print(type(True)) # <class 'bool'>
print(type(1)) # <class 'int'>
print('bool是否为int的子类：', issubclass(bool, int)) # True
print('True的int值为1：', True == 1) # True
print('bool逻辑运算符 and、or、not:', (True or False) and (True) and not False) # True
# 在 Python 中，所有非零的数字和非空的字符串、列表、元组等数据类型都被视为 True，
# 只有 0、空字符串、空列表、空元组等被视为 False。
# 因此，在进行布尔类型转换时，需要注意数据类型的真假性。

# 删除对象引用
del a, b, c

# 数值运算
# 在混合计算时，Python会把整型转换成为浮点数
print(2 / 4)  # 除法，得到一个浮点数 0.5
print(2 // 4) # 除法，得到一个整数 0
print(2 ** 4) # 乘方 16
print(5%3) # 取余 2

print((1.55 + 0.45) * 1) # 2.0

a = '单引号'
b = "双引号"
print('\\转义')
print(r'\\\n不用r(raw)开头则不转义')


# 集合类型的数据赋值
# 列表使用 [], 可以修改
list = ['a', 'b', True, 1.5, '类型可以不一致']
list[1] = 'c'
print('append操作返回值:', list.append('app')) # None
print('pop:', list.pop()) # app
list2 = ['a', 'b'] + [1, True] # append操作

# 元组使用括号 (),元素类型也可以不相同, 但不能修改
tuple1 = ('江苏', '浙江')
tuple2 = ('上海',) # 如果只有一个值，需要用逗号，以区分数值运算中的括号
tuple3 = tuple1 + tuple2 # append操作不是修改，而是得到新的元组对象

# 集合set
# 集合使用 {}，无序，可修改，不重复（自动去重）
set1 = {1,2,3,2}
# 空集合只能用 set(), {}用于创建空字典
empty_set = set() # 不能有变量名为set
'''
set = 5  # 错误地覆盖了内置的 set 类型
empty_set = set()  # 这会引发 TypeError: 'set' object is not callable，因为 set 现在是整数 5
'''
# 可以进行交集、并集、差集等常见的集合操作
set2 = {3,4,5}
print(1 in set1)
print(10 not in set1)
print(set1 - set2) # 差集
print(set1 | set2) # 并集
print(set1 & set2) # 交集
print(set1 ^ set2) # a 和 b 中不同时存在的元素(交集以外的数据)

# set() 入参是一个sequence
set3 = set('abc') # 等价 {'a', 'b', 'c'}
print(set3)


# Dictionary（字典）Java中的Map
# 键(key)必须使用不可变类型
dict0 = {}
dict1 = {'a': 1, 'b': 'bb'}
dict2 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
dict3 = dict(Runoob=1, Google=2, Taobao=3)
print(dict3)
print(dict1.get('a'))
print(dict1['a'])
dict1['a'] = 'a'
dict1['c'] = 'c'
dict1.setdefault('d', 'dd')
print(dict1)

# ** 用于字典解包（也称为字典拆包或字典展开）
# 1、在子字典合并中解包字典
dict1 = {'a': 1, 'b': '2'}
dict2 = {'c': 3, 'd': '4'}
dict3 = {**dict1, **dict2}
print(dict3)

# 2、在函数定义中收集关键字参数
def func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

func(a=1, b=2, c=3)
# 输出：
# a: 1
# b: 2
# c: 3

# 3、在函数调用中解包字典
# 字典的键必须与函数期望的参数名匹配。如果字典中包含函数不期望的键，或者缺少函数需要的键，会引发错误（少参数的情况，除非函数有默认值）。
def func(a, b, c):
    print(a, b, c)

params = {'a': 1, 'b': 2, 'c': 3}
func(**params)  # 输出：1 2 3



# <class 'bytes'> bytes 类型表示的是不可变的二进制序列
x = bytes('hello', "utf-8")
print(x) # b'hello'
print(type(x)) # <class 'bytes'>
# 用b开头创建bytes
y = b'world'
print(y)
print(y[0]) # 119 bytes类型中的元素是整数值


