# 逻辑运算符
'''
and  or not  对应Java中的 &&  ||  !  符号

Python不支持 &&, ||, ! 符号,  支持按位 与& 异^  或|
'''
print(0 and 10) # 0
print(1 and 10) # 10
print(2 and 10) # 10

print(1 or 10) # 1
print(2 or 10) # 2
print(0 or 10) # 10

print(not 1) # False