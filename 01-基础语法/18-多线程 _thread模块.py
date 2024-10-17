import _thread
import time

'''
函数式：
_thread.start_new_thread (function, args[, kwargs] )
args 必须为tuple类型

（Python2中线程的模块名称为 thread）

'''


# 为线程定义一个函数
def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f"{thread_name} {time.ctime(time.time())}")


# 创建两个线程
try:
    _thread.start_new_thread(print_time, ("Thread-1", 2,))
    _thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print("Error: 无法启动线程")

# 控制主线程等待不结束
while 1:
    pass

