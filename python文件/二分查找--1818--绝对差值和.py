__time__ = '2021/7/14'
__author__ = 'ZhiYong Sun'

from typing import List
import bisect

"""
1818--绝对差值和
给你两个正整数数组 nums1 和 nums2 ，数组的长度都是 n 。

数组 nums1 和 nums2 的 绝对差值和 定义为所有 |nums1[i] - nums2[i]|（0 <= i < n）的 总和（下标从 0 开始）。

你可以选用 nums1 中的 任意一个 元素来替换 nums1 中的 至多 一个元素，以 最小化 绝对差值和。

在替换数组 nums1 中最多一个元素 之后 ，返回最小绝对差值和。因为答案可能很大，所以需要对 109 + 7 取余 后返回。
"""


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        size = len(nums1)
        sums = 0
        max_diff = 0

        for i in range(size):
            sums += abs(nums1[i] - nums2[i])
        if sums == 0:
            return 0

        temp = sorted(nums1)
        for ind, num in enumerate(nums2):
            diff = abs(nums1[ind] - num)
            if diff <= max_diff:
                continue
            else:
                left = bisect.bisect_left(temp, num)
                if left >= 1:
                    max_diff = max(max_diff, diff-(num-temp[left-1]))
                if left < size:
                    max_diff = max(max_diff, diff-(temp[left]-num))

        return int((sums - max_diff) % (10e9 + 7))


if __name__ == '__main__':
    nums1 = [1, 10, 4, 4, 2, 7]
    nums2 = [9, 3, 5, 1, 7, 4]
    print(Solution().minAbsoluteSumDiff(nums1, nums2))

