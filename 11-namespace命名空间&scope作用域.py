'''
一般有三种命名空间：
1、内置名称（built-in names）， Python 语言内置的名称，比如函数名 abs、chr 和异常名称 BaseException、Exception 等等。
2、全局名称（global names），模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
3、局部名称（local names），函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）

命名空间查找顺序: 局部的命名空间 -> 全局命名空间 -> 内置命名空间
如果找不到变量 xxx，它将放弃查找并引发一个 NameError 异常
'''

print(abs(-1))
print(chr(65))

# raise Exception

# 作用域就是一个 Python 程序可以直接访问命名空间的正文区域。
'''
有四种作用域：
1、L（Local）：最内层，包含局部变量，比如一个函数/方法内部。
2、E（Enclosing）：包含了非局部(non-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
3、G（Global）：当前脚本的最外层，比如当前模块的全局变量。
4、B（Built-in）： 包含了内建的变量/关键字等，最后被搜索。

查找顺序： L –> E –> G –> B
'''

# 全局变量和局部变量
# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
total = 0  # 这是一个全局变量
# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total
# 调用sum函数
sum(10, 20) # 30
print("函数外是全局变量 : ", total) # 0

# global 和 nonlocal关键字
# 当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了。

# 修改全局变量用global
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num) # 1
    num = 123
    print(num) # 123
fun1() # 1 123
print(num) # 123

# 修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num) # 100
    inner()
    print(num) # 100
outer() # 输出 100 100


a = 10
def test():
    # 报错 UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
    # 因为 a + 1中的a在局部未定义
    a = a + 1
    print(a)
test()