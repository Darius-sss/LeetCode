__time__ = '2021/7/15'
__author__ = 'ZhiYong Sun'

import bisect

"""给定一个n个元素有序的（升序）整型数组nums 和一个目标值target ，
写一个函数搜索nums中的 target，如果目标值存在返回下标，否则返回 -1。

"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:  # 标准二分法框架
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + ((right - left) >> 1)  # 之所以这么写是为了避免大数溢出问题
            if nums[mid] == target: return mid
            elif nums[mid] < target: left = mid + 1
            else: right = mid - 1
        return -1


class Solution_use_bisect:
    def search(self, nums: List[int], target: int) -> int:
        # 调用bisect二分库的解法，这道题是考察二分法，不可这么用，只是提供一个思路
        index = bisect.bisect_left(nums, target)
        if index == len(nums) or nums[index] != target:
            return -1
        return index


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(Solution().search(nums, target))
    print(Solution_use_bisect().search(nums, target))