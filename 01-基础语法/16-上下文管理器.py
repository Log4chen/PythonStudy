'''
上下文管理器
在一个类MyClass里，实现了__enter__和__exit__的方法，这个类的实例就是一个上下文管理器。
以下3行代码，会按顺序执行如下：
    - 执行MyClass的构造方法 init
    - 执行 enter 方法
    - 将创建的MyClass实例赋值为res
    - 调用 do_something() 方法
    - 如果do_something()没有抛出异常，执行print(1)
    - 执行 exit 方法；如果do_something()抛出异常，exit入参 exc_* 3个参数不为None
    - 执行print(2)

with MyClass() as res:
    res.do_something()
    print(1)
print(2)

'''

class MyClass():
    exc_type = None
    exc_val = None
    exc_tb = None
    def __init__(self):
        print('init')
    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exc_type = exc_type
        self.exc_val = exc_val
        self.exc_tb = exc_tb
        print(f'exc_type：{type(exc_type)} exc_val:{type(exc_val)} exc_tb:{type(exc_tb)}')
        print('exit')
        return self

    def do_something(self, i:int):
        print('do something')
        if i == 1:
            raise ValueError('value is 1')

with MyClass() as res:
    res.do_something(2)
    print('do_something没有抛出异常，这一行执行')

with MyClass() as res:
    res.do_something(1)
    print('do_something抛出异常，这一行不执行')
print(res.exc_type)
print(res.exc_val)
print(res.exc_tb)

# 不新建类使用上下文管理
# yield之前的代码，就相当于__enter__里的内容。yield 之后的代码，就相当于__exit__ 里的内容
import contextlib

@contextlib.contextmanager
def open_func(file_name):
    # __enter__方法
    print('open file:', file_name, 'in __enter__')
    file_handler = open(file_name, 'r')

    try:
        yield file_handler # yield表达式后的值，会被赋值给with语句中as后面的变量
    except Exception as exc:
        # deal with exception
        print('the exception was thrown')
    finally:
        print('close file:', file_name, 'in __exit__')
        file_handler.close()

        return

print('=================================')
with open_func('./data.json') as file_in: # file_in 为 yield 后面的对象
    print(type(file_in)) # <class '_io.TextIOWrapper'>
    for line in file_in:
        print(line)
    raise TypeError('type is error')
    print(1)
print(2)
