__time__ = '2021/7/29'
__author__ = 'ZhiYong Sun'

from typing import List

"""
给定一个包含n 个整数的数组nums和一个目标值target，判断nums中是否存在四个元素 a，b，c和 d，

使得a + b + c + d的值与target相等？找出所有满足条件且不重复的四元组。

注意：答案中不可以包含重复的四元组。
"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        size = len(nums)
        if size < 4: return []   #  数字少于四个，则直接返回

        nums.sort()
        for i in range(size - 3):
            if i > 0 and nums[i] == nums[i - 1]: continue   # 避免第一个数字重复
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target: break    # 优化 -- 最小的四个数字和就比target大，则退出
            if nums[i] + nums[size-1] + nums[size-2] + nums[size-3] < target: continue  # 优化 -- 选择i时，最大的情况都小于target，则不用在继续比较了

            for j in range(i + 1, size - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: continue   # 避免第二个数字重复
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target: break    # 优化 -- 最小的四个数字和就比target大，则退出
                if nums[i] + nums[j] + nums[size-1] + nums[size-2] < target: continue  # 优化 -- 选择i时，最大的情况都小于target，则不用在继续比较了
                left, right = j + 1, size - 1

                while left < right:
                    sum_ = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum_ == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left+1] == nums[left]: left += 1    # 避免第三个数字重复
                        while left < right and nums[right-1] == nums[right]: right -=1   # 避免第四个数字重复
                        left += 1
                        right -= 1
                    elif sum_ < target:
                        left += 1
                    else:
                        right -= 1
        return res


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(Solution().fourSum(nums, target))