__time__ = '2021/7/4'
__author__ = 'ZhiYong Sun'

"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0: return 0
        if n <= 2: return n
        first, second = 1, 2
        for _ in range(3, n+1):
            first, second = second, first + second
        print(second)
        return second

if __name__ == "__main__":
    for num in range(20):
        Solution().climbStairs(num)