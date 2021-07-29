__time__ = '2021/7/29'
__author__ = 'ZhiYong Sun'

from typing import List

"""
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
"""

# 为什么要逆序？是因为dp后面的和的情况是从前面的情况转移过来的，如果前面的情况因为当前nums[i]的加入变为了True，
# 比如dp[0 + nums[i]]变成了True，那么因为一个数只能用一次，dp[0 + nums[i] + nums[i]]不可以从dp[0 + nums[i]]转移过来。
# 如果非要正序遍历，必须要多一个数组用于存储之前的情况。而逆序遍历可以省掉这个数组
# ps：正序情况见题0332--零钱兑换


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, sum_ = len(nums), sum(nums)
        if n < 2 or sum_ & 1 or max(nums) > sum_ >> 1: return False    # 如果不足两个数字 或总和是奇数 或最大值大于总和的一半 则直接返回
        target = sum_ >> 1

        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):   # 不可以使用重复数字 --> 逆序遍历  当前遍历过的不会影响到当前之后遍历的部分
                dp[j] = dp[j] or dp[j - nums[i]]
        return dp[-1]


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    print(Solution().canPartition(nums))