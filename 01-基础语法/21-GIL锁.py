'''
参考：https://zhuanlan.zhihu.com/p/647005743

GIL全名为全局解释器锁（Global Interpreter Lock）。
这是一种线程管理机制，并不根属于Python语言，而是存在于CPython中。
Cpython是由官方推出、用C语言实现的Python代码解释器。
换言之，只要用的Python是官方版本，都会受到GIL的影响。

在GIL锁开启的情况下，同个进程内的多个线程只能串行而不能并行。
GIL的释放有两种触发方式，一种是遇到I/O操作，另一种则是超出时间限制。
遇到I/O操作时，原线程运行结束，其余线程对CPU使用权进行「竞争」。
但如果是超时释放，原来运行的线程会重新加入这场「竞争」。

避免GIL锁影响多CPU性能，可以使用多进程 multiprocessing

CPython未来的版本中，将提供可选择性关闭GIL。
'''