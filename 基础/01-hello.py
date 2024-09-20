#!/usr/bin/python

print("Hello, World!")

'''
#!/usr/bin/python
在Unix和Linux系统上的脚本文件的第一行，告诉操作系统执行这个脚本的时候，调用 /usr/bin 下的 python 解释器。
这样就可以直接 './hello.py' 运行（需要对文件赋权 chmod +x hello.py），而不需要调用 'python hello.py'。

#!/usr/bin/env python
这种用法是为了防止操作系统用户没有将 python 装在默认的 /usr/bin 路径里。
系统会查找用户 PATH 环境变量中第一个匹配 python 的解释器，并使用该解释器来执行脚本。
'''