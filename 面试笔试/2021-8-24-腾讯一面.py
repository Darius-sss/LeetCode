__time__ = '2021/8/24'
__author__ = 'ZhiYong Sun'

"""
python垃圾回收机制
进程、线程、协程联系与区别
讲一下GIL
讲一下在联影做的后端测试（算法一致性和性能测试）
。。。
"""


""" n个球中有一个比其他的重，其他的都一样，最少至多寻找多少次可以找到"""


def check(n):
    count = 0
    while n != 1:
        if n % 4 == 0:
            n = (n-2) / 2
        elif n % 2 == 0:
            n /= 2
        else:
            n = (n-1) / 2
        count += 1
    return count


if __name__ == '__main__':
    for i in range(1, 9):
        print(check(i))



