'''
在Python中，yield 是一个关键字，用于定义生成器（generator）函数。
生成器是一种特殊的迭代器，可以在需要时产生值，而不是一次性生成一个包含所有值的列表。
这使得生成器特别适合用于处理大量数据或无限数据的场景，因为它们可以更高效地使用内存。
'''


'''
当你使用 yield 关键字在一个函数中时，这个函数就变成了一个生成器函数。
每次调用 yield 时，它会生成一个值，然后函数会暂停执行，直到下一次迭代。
'''
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        print('count+1')
        count += 1

counter = count_up_to(3)
print('生成器不会一次性把所有值加载到内存中')
for number in counter:
    print(number)
