__time__ = '2021/7/29'
__author__ = 'ZhiYong Sun'

from typing import List

"""
给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i >= 1 and nums[i] == nums[i - 1]:  # 保证不重复
                continue
            left, right = i + 1, len(nums) - 1

            while left < right:
                sum_ = nums[left] + nums[right] + nums[i]
                if sum_ == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left + 1] == nums[left]: left += 1
                    while left < right and nums[right - 1] == nums[right]: right -= 1
                    left += 1
                    right -= 1
                elif sum_ < 0:
                    left += 1
                else:
                    right -= 1
        return res


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))