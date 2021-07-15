__time__ = '2021/7/15'
__author__ = 'ZhiYong Sun'

import bisect

"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。
"""

from typing import  List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)   # 这里的right从len(nums)开始，是比较少见的情况

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == "__main__":
    nums = [1, 3, 5, 7, 8]
    target = 9
    print(Solution().searchInsert(nums, target))

    # 该问题可以直接调库解决
    print(bisect.bisect_left(nums, target))