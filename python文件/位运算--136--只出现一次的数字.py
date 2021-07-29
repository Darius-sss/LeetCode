__time__ = '2021/7/28'
__author__ = 'ZhiYong Sun'

from operator import xor
from typing import List
from functools import reduce

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 根据 相同数字的异或结果为0--这是最好的办法----初次之外，这道题可以使用数学方法
        return reduce(xor, nums)


class Solution_math:
    def singleNumber(self, nums: List[int]) -> int:
        # 数学方法
        return 2 * sum(set(nums)) - sum(nums)


if __name__ == "__main__":
    nums = [1, 2, 1, 2, 3, 4, 5, 5, 4]
    print(Solution_math().singleNumber(nums))
    print(Solution().singleNumber(nums))