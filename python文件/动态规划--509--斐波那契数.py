__time__ = '2021/7/29'
__author__ = 'ZhiYong Sun'


"""
斐波那契数，通常用F(n) 表示，形成的序列称为 斐波那契数列 。该数列由0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1)= 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给你 n ，请计算 F(n) 。
"""


class Solution:
    def fib(self, n: int) -> int:
        l, r = 0, 1
        for _ in range(n):
            l, r = r, l + r
        return l


if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5, 90]
    for n in nums:
        print(Solution().fib(n))