__time__ = '2021/7/6'
__author__ = 'ZhiYong Sun'

from typing import List

"""
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for ind, num in enumerate(nums):
            if target - num in hashmap:
                print([hashmap[target-num], ind])
                return [hashmap[target-num], ind]
            hashmap[num] = ind


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 18
    Solution().twoSum(nums, target)