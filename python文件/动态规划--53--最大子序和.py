__time__ = '2021/7/29'
__author__ = 'ZhiYong Sun'

from typing import List

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-float('inf')] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = max(nums[i-1], dp[i-1] + nums[i-1])   # 转移方程 -- 对于当前数字来说，要么是自己，要么是加上前面一个位置的值
        return max(dp)


if __name__ == "__main__":
    nums = [-2]
    print(Solution().maxSubArray(nums))
