__time__ = '2021/7/28'
__author__ = 'ZhiYong Sun'
__doc__ = '判断一个数是否是2的幂'


"""
给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

如果存在一个整数 x 使得n == 2x ，则认为 n 是 2 的幂次方。
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 如果是2的幂次方 则二进制只有一个1
        return n > 0 and n & (n - 1) == 0


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 32, 64, 127]
    for num in nums:
        print(Solution().isPowerOfTwo(num))
