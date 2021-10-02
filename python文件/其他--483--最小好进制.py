__time__ = '2021/7/30'
__author__ = 'ZhiYong Sun'
__doc__ = 'https://leetcode-cn.com/problems/smallest-good-base/solution/python-ren-xing-de-py100-by-qubenhao-6kvg/'

"""

对于给定的整数 n, 如果n的k（k>=2）进制数的所有数位全为1，则称 k（k>=2）是 n 的一个好进制。

以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。
"""


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        # 由数学证明得到两个性质：
        # 一：m < logkn  -- >  m < 60
        # 二：k = [pow(n, 1/m)]

        n = int(n)
        for m in range(n.bit_length(), 2, -1):
            k = int(pow(n, 1 / (m-1)))

            if (1-k ** m) // (1-k) == n:
                return str(k)

        return str(n - 1)


if __name__ == "__main__":
    print(Solution().smallestGoodBase("2251799813685247"))
    print(Solution().smallestGoodBase("8"))
    print(Solution().smallestGoodBase("4681"))