import time

print("============time====================")
print(f'时间戳：{time.time()}')

localtime = time.localtime()
print("本地时间：", localtime)

# 取年、月、日、时、分、秒等
print(f'{localtime.tm_year}-{localtime.tm_mon}-{localtime.tm_mday} {localtime.tm_hour}:{localtime.tm_min}:{localtime.tm_sec}')

# 格式化
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

# 线程sleep
time.sleep(2)

