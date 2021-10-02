__time__ = '2021/7/4'
__author__ = 'ZhiYong Sun'

"""给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0

        # 状态数组dp[i]=[mx, mn] 表示 走到第i位置 的最大，最小乘积
        size = len(nums)
        mx, mn = nums[0], nums[0]  # 状态
        result = nums[0]

        # 状态转移
        # 到当前最大子乘积：必须包含自己， 存在三种情况
        for i in range(1, size):
            mx, mn = max(mx * nums[i], mn * nums[i], nums[i]), min(mx * nums[i], mn * nums[i], nums[i])
            result = max(result, mx)
        print(result)
        return result


if __name__ == "__main__":
    nums = []
    nums.append([2, 3, -2, 4])
    nums.append([-2, 0, -1])
    nums.append([-4, -3, -2])
    for num in nums:
        Solution().maxProduct(num)
