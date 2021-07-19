__time__ = '2021/7/19'
__author__ = 'ZhiYong Sun'

"""
元素的 频数 是该元素在一个数组中出现的次数。

给你一个整数数组 nums 和一个整数 k 。在一步操作中，你可以选择 nums 的一个下标，并将该下标对应元素的值增加 1 。

执行最多 k 次操作后，返回数组中最高频元素的 最大可能频数 。

"""

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()   # 滑动窗口问题一般都需要排序
        left, right = 0, 1   # 窗口初始的左右位置
        total, count = 0, 1  # 初始时填充的差值 和 频数

        while right < len(nums):
            total += (right - left) * (nums[right] - nums[right - 1])  # 每次右边窗口右移时需要的差值
            while total > k:
                total -= nums[right] - nums[left]   # 当total大于k时，此时将左边窗口进行右移
                left += 1
            count = max(count, right - left + 1)
            right += 1
        return count


if __name__ == "__main__":
    nums = [1, 4, 6, 7, 2, 4, 6, 8, 9, 3]
    print(Solution().maxFrequency(nums, 13))


"""
窗口滑动问题的模板：
left,right = 0, (0 or 1)
res = total = 0
while right < len(nums):
   更新total值
   while 窗口内数据不满足要求
      1. 更新total值
      2. 收缩左边界
   更新res最大值
返回 res
"""