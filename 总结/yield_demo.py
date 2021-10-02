__time__ = '2021/9/10'
__author__ = 'ZhiYong Sun'


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 使用 yield
        a, b = b, a + b
        n = n + 1



print(type(fab(5)))     # <class 'generator'>
print(list(fab(5)))    # [1, 1, 2, 3, 5]  可以按需生成并“返回”结果，而不是一次性产生所有的返回值

print(type((x*x for x in range(4))))   # 对<'generator'>进行迭代,随着RANGE_NUM的变大,没有任何区别
print(type([x*x for x in range(4)]))   # 对<'list'>进行迭代, 随着RANGE_NUM的变大，返回的列表也越大，占用的内存也越大
