__time__ = '2021/7/29'
__author__ = 'ZhiYong Sun'

from typing import List

"""
给定一个已按照 升序排列 的整数数组numbers ，请你从数组中找出两个数满足相加之和等于目标数target 。

函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。

你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。

"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 有序数组 -- 使用双指针
        left, right = 0, len(numbers) - 1
        while left < right:
            sum_ = numbers[left] + numbers[right]
            if sum_ == target:
                return [left+1, right+1]
            elif sum_ < target:
                left += 1
            else:
                right -= 1


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(numbers, target))

    numbers = [2, 3, 4]
    target = 6
    print(Solution().twoSum(numbers, target))