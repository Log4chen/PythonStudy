# try...except...else...finally
def f(i: int):
    try:
        print('try')
        if i == 1:
            raise TypeError('error msg')
    except TypeError as error: # 捕获到异常
        print(error.args)
    else: # 如果没有异常执行else
        print('else')
    finally:
        print('finally')
f(2)
f(1)

'''
上下文管理器
'''

# with  封装了try...except...finally
file = open('./test_runoob.txt', 'w') # file类型 <class '_io.TextIOWrapper'>
try:
    file.write('hello world')
finally: #即使发生异常也会执行finally关闭文件
    file.close()

# 使用 with 关键字系统会自动调用 file.close() 方法， with 的作用等效于 try/finally 语句是一样的
with open('./test_runoob.txt', 'w') as file:
    file.write('hello world !')

'''
with 语句实现原理建立在上下文管理器之上。
上下文管理器是一个实现 __enter__ 和 __exit__ 方法的类。
使用 with 语句确保在嵌套块的末尾调用 __exit__ 方法。

在文件对象中定义了 __enter__ 和 __exit__ 方法，即文件对象也实现了上下文管理器，
首先调用 __enter__ 方法，然后执行 with 语句中的代码，最后调用 __exit__ 方法。 
即使出现错误，也会调用 __exit__ 方法，也就是会关闭文件流。


'''
