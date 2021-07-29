__time__ = '2021/7/29'
__author__ = 'ZhiYong Sun'
__doc__ = '单调栈'

from typing import List

"""
给你两个 没有重复元素 的数组nums1 和nums2，其中nums1是nums2的子集。

请你找出 nums1中每个元素在nums2中的下一个比其大的值。

nums1中数字x的下一个更大元素是指x在nums2中对应位置的右边的第一个比x大的元素。如果不存在，对应位置输出 -1 。
"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = {}

        for num in nums2:
            while stack and num > stack[-1]:   # 单调栈
                hashmap[stack.pop()] = num
            stack.append(num)

        return [hashmap.get(num, -1) for num in nums1]    #  虽然知道get函数，但是在这里使用是很巧妙的


if __name__ == "__main__":
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    print(Solution().nextGreaterElement(nums1, nums2))

    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(Solution().nextGreaterElement(nums1, nums2))
