__time__ = '2021/7/20'
__author__ = 'ZhiYong Sun'

"""
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

"""


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3: return n - 1    # 题目中 n > 1
        i, j = divmod(n - 2, 3)    # 这么做是由于4这个数的特殊性，只有一个4的话不拆分乘积才是最大的
        return (j + 2) * 3 ** i


if __name__ == "__main__":
    nums = list(range(5, 25))
    for n in nums:
        print(n, Solution().cuttingRope(n))