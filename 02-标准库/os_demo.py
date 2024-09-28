import os

print(os.path.abspath(""))

# 打开文件
fd = os.open("os_demo.py", os.O_RDONLY)
print(type(fd)) # integer

# 读取文本
data = os.read(fd, 1024) # bytes
print(data.decode("utf-8"))

# 关闭文件
os.close(fd)

