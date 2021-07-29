__time__ = '2021/7/29'
__author__ = 'ZhiYong Sun'
__doc__ = '单调栈'


"""
给你一个整数数组 nums ，数组中共有 n 个整数。132 模式的子序列 由三个整数 nums[i]、nums[j] 和 nums[k] 组成，并同时满足：i < j < k 和

nums[i] < nums[k] < nums[j] 。

如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。
"""


from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        candidate_k = [nums[n - 1]]
        max_k = float("-inf")

        for i in range(n - 2, -1, -1):
            if nums[i] < max_k:
                return True
            while candidate_k and nums[i] > candidate_k[-1]:   # 使得max_k小于nums[i]并且尽可能大
                max_k = candidate_k[-1]
                candidate_k.pop()
            if nums[i] > max_k:      # 如果nums[i]比max_k还要大，那么将其添加到单调栈中
                candidate_k.append(nums[i])

        return False


if __name__ == '__main__':
    nums = [3, 1, 4, 2]
    print(Solution().find132pattern(nums))

    nums = [-1, 3, 2, 0]
    print(Solution().find132pattern(nums))

    nums = [1, 2, 3, 4]
    print(Solution().find132pattern(nums))