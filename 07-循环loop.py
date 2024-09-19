# Python不支持 do while
sum = 0
i = 1
while i <= 100:
    sum = sum + i
    i += 1

print("1 到 %d 之和为: %d" % (100, sum))

# while else
# 如果 while 后面的条件语句为 false 时，则执行 else 的语句块
count = 0
while count < 5:
   print(count, " 小于 5")
   count = count + 1
else:
   print(count, " 大于或等于 5")

# for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串
# Python不能用for Java中的 for(int i = 0; i < 10; i++) do something
'''
for <variable> in <sequence>:
    <statements>
else:
    <statements>
'''

# while或者for的else代码块，只有正常结束循环时才会执行，如果是通过break退出循环，则不会执行else