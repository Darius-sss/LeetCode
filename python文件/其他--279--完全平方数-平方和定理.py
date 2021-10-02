__time__ = '2021/7/30'
__author__ = 'ZhiYong Sun'
__doc__ = '平方和定理'
"""
给定正整数n，找到若干个完全平方数（比如1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
"""

"""
四平方和定理：任何一个整数都可以由四个数的平方和组成
三平方和定理：所有不满足(4**m)(8*k+7)形式的数都可以由三个数的平方和组成
二平方和定理：暂无
"""
import math


class Solution:
    def numSquares(self, n: int) -> int:
        # 平方和定理--4m(8k+7)

        def isSquares(n):
            return int(math.sqrt(n)) ** 2 == n

        # 三平方和定理 + 四平方和定理
        while n & 3 == 0:
            n >>= 2
        if n & 7 == 7:
            return 4

        if isSquares(n):
            return 1

        for i in range(int(math.sqrt(n)) + 1):
            if isSquares(n - i ** 2):
                return 2

        return 3


if __name__ == "__main__":
    for n in [7, 15, 4, 2, 8, 99]:
        print(Solution().numSquares(n))