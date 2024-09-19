'''
Python 数据类型转换可以分为两种
- 隐式转换 - 自动 (仅限数值)
- 显式转换 - 一般情况下你只需要将数据类型作为函数名即可
'''

print(int(1.6)) # 输出1
print(int('1')) # int('1.5') 会报错，需要要float('1.5')

print(float(1))
print(float('1.5'))

print(str(1.5))