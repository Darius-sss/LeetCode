__time__ = '2021/7/6'
__author__ = 'ZhiYong Sun'

from typing import List

"""
 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
 
 求解：如果算法时间复杂度没有要求的话，直接排序取中间即可 O(m+n)
 以下解法时间复杂度为 O(log(min(m,n))
"""


# 思路就是对于其中一个数组进行二分，另一个数组根据左边一共有 (m+n+1)//2 个元素进行划分
# 输出的断点：nums1[i] < nums2[j] 且 nums1[j-1] < nums2[i+1], 也就是说左边的数都比右边小，并且左边有(m+n+1)//2个数

# 细节优化：
# 1. 对长度小的数组进行二分；
# 2. (m+n+1)//2 表明如果(m+n)是奇数，则中位数在为左边数的最大数；
# 3. 如果nums1划分到0或者m这两个位置，划分到0是nums1左侧为 负无穷大， 划分到m时右侧为 正无穷大， nums2也一样


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 在这里保证了m<=n，从而保证nums2_ind非负
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            # return self.findMedianSortedArrays(nums2, nums1)   # 或者使用递归也行，注意return
        m, n = len(nums1), len(nums2)
        infinity = 2 ** 32
        left, right = 0, m
        max_left, min_right = 0, 0

        while left <= right:
            # nums1_ind+nums2_ind始终等于（m+n+1)//2
            nums1_ind = (left + right) // 2
            nums2_ind = (m + n + 1) // 2 - nums1_ind

            # 还需要进一步理解
            nums1_mid_left = -infinity if nums1_ind == 0 else nums1[nums1_ind - 1]
            nums1_mid_right = infinity if nums1_ind == m else nums1[nums1_ind]
            nums2_mid_left = -infinity if nums2_ind == 0 else nums2[nums2_ind - 1]
            nums2_mid_right = infinity if nums2_ind == n else nums2[nums2_ind]

            if nums1_mid_left <= nums2_mid_right:
                max_left, min_right = max(nums1_mid_left, nums2_mid_left), min(nums1_mid_right, nums2_mid_right)
                left = nums1_ind + 1
            else:
                right = nums1_ind - 1

        return max_left if (m + n) & 1 else (max_left + min_right) / 2


if __name__ == "__main__":
    nums1 = [2]
    nums2 = []
    result = Solution().findMedianSortedArrays(nums1, nums2)
    print(result)

