__time__ = '2021/7/20'
__author__ = 'ZhiYong Sun'

"""输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。"""

from typing import List


class Solution:   # 思路----当左指针为偶数，右指针为奇数时，进行原地调换
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] & 1:
                i += 1
            elif not nums[j] & 1:
                j -= 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == "__main__":
    nums = [2, 16, 3, 5, 13, 1, 16, 1, 12, 18, 11, 8, 11, 11, 5, 1]
    print(Solution().exchange(nums))

    # 如果要保持顺序的话可以通过一次遍历来重新构造列表，但是需要额外空间
    nums1 = [2, 16, 3, 5, 13, 1, 16, 1, 12, 18, 11, 8, 11, 11, 5, 1]
    print([num for num in nums1 if num & 1] + [num for num in nums1 if not num & 1])