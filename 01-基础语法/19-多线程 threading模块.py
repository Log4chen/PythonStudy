import threading
import time

'''
类模式

'''


# 为线程定义一个函数
def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f"{thread_name} {time.ctime(time.time())}")


# 创建线程
t1 = threading.Thread(target=print_time, args=("Thread-1", 1,), daemon=False)
t2 = threading.Thread(target=print_time, args=("Thread-2", 2,), daemon=False)

# 启动线程
t1.start()
t2.start()

# 等待线程结束
t1.join()
print('thread 1 结束')

t2.join()
print('thread 2 结束')


# 继承threading.Thread
class myThread(threading.Thread):
    def __init__(self, thread_id, name, delay):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.delay = delay

    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.delay)
        print("退出线程：" + self.name)


t3 = myThread(3, 'Thread-3', 4)
t3.start()
t3.join()

# 互斥锁
# 不可重入：一旦线程拥有了一个Lock对象，它不能再次调用acquire()来获取同一个锁，否则会导致死锁。
threadLock = threading.Lock()
threadLock.acquire()
# threadLock.acquire()  # 不可重入，会导致线程一直等待
threadLock.release()

'''
可重入锁：允许同一个线程多次获取同一个锁，而不会发生死锁
可重入性：如果一个线程已经拥有了一个RLock，当它再次调用acquire()时，调用会成功，并且锁的计数会增加。
        每次成功的acquire()调用都必须有一个对应的release()调用，以返回到上一个计数或完全释放锁。
        只有当锁的计数回到零时，锁才真正被释放，其他线程才能获取它。
'''
reentrantLock = threading.RLock()
reentrantLock.acquire()
reentrantLock.acquire()
reentrantLock.release()
reentrantLock.release()
