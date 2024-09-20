'''
Python 推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体。

Python 推导式是一种强大且简洁的语法，适用于生成列表、字典、集合和生成器。

相当于Java中的 seq.stream().map(x- > return y).collection(Collectors.toList())
'''

list = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_list = [name.upper() for name in list if(len(name) > 3)]
print(new_list)
print([name.upper() for name in list])

# 字典推导式
'''
{ key_expr: value_expr for value in collection }

或

{ key_expr: value_expr for value in collection if condition }
'''

# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
print({key: len(key) for key in list})

# set集合推导式
'''
{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }
'''
list = ['a', 'b','c','a']
print({str + "_" for str in list}) # {'b', 'a', 'c'}

# 元组推导式（生成器表达式）
# 元组推导式返回的结果是一个生成器对象
a = (x for x in range(1,10))
print(a) # <generator object <genexpr> at 0x000002373F55CE80>
# # 使用 tuple() 函数，可以直接将生成器对象转换成元组
print(tuple(a)) # (1, 2, 3, 4, 5, 6, 7, 8, 9)