def hello(name, age, c = '默认参数'):
    print(f'{name} is {age} {c}')

# 按顺序传参方式
hello('tony', '20')

# 关键字入参方式
hello(age=30, name='tony', c = 'abc')

# 不定长参数
# 加*的参数会以元组(tuple)的形式导入，可以是空元组
# * 后的参数必须用关键字传入
def helloword(arg1, *arg_tuple, d):
    print(arg1)
    print(type(arg_tuple))
    print(arg_tuple)
    print(d)

helloword('元组', 1,2,'a', d=1)

# 两个星号 ** 的参数会以字典的形式导入
def helloword2(arg1, **arg_dict):
    print(arg1)
    print(type(arg_dict))
    print(arg_dict)

helloword2('字典', a=1,b=2)

# 使用lambda创建匿名函数
'''
lambda [arg1 [,arg2,.....argn]]:expression
'''
c = 10
x = lambda a, b: a + b + c
print(x(1, 2))