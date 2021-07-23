__time__ = '2021/7/20'
__author__ = 'ZhiYong Sun'

from typing import List

"""
一个数对(a,b)的 数对和等于a + b。最大数对和是一个数对数组中最大的数对和。

比方说，如果我们有数对(1,5)，(2,3)和(4,4)，最大数对和为max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8。
给你一个长度为 偶数n的数组nums，请你将 nums中的元素分成 n / 2个数对，使得：

nums中每个元素恰好在 一个数对中，且最大数对和的值 最小。
请你在最优数对划分的方案下，返回最小的 最大数对和。

"""
# 解法：排序后最大的好最小的组合，然后比较即可


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = -float('inf')
        size = len(nums)
        for i in range(size >> 1):
            res = max(res, nums[i] + nums[size - i - 1])
        return res


if __name__ == "__main__":
    nums = [3,5,2,3, 4, 5,6, 8, 9, 2, 4, 6]
    print(Solution().minPairSum(nums))