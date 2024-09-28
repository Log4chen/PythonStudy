import keyword as k

# 保留字
print(k.kwlist)

# 标识符
'''
第一个字符必须是字母表中字母或下划线 _ 。
标识符的其他的部分由字母、数字和下划线组成。
标识符对大小写敏感。
'''
a = 1
_a = 1
_a1 = 1

# 多行语句 & 单行语句
'''
1、多行语句，反斜杠 '\'  换行；在 [], {}, 或 () 中的多行语句，不需要使用反斜杠
2、同一行显示多条语句，用分号 ; 分割
'''
total = 1 + 2 \
    + 3

i = 1; j = 2; print(i+j)

# 多个语句构成代码组, 缩进相同的一组语句构成一个代码块，我们称之代码组。
if i == 1:
    print(1)
    print(2)
else:
    print(3)
    print(4)

# 不换行输出
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""
print('tony')
print('hello ', end='')
print('world')

# import
'''
将整个模块(somemodule)导入，格式为： import somemodule [as xxx 起别名]
从某个模块中导入某个函数,格式为： from somemodule import somefunction [as xxx 起别名]
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
'''
import sys
print ('命令行参数为:')
for i in sys.argv:
    print(i)
print('python 路径为',sys.path)

print("===============================")
x = 10
print("是的" if x > 5 else "不是")

a = []
print('是的' if a else '不是')