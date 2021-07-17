__time__ = '2021/7/16'
__author__ = 'ZhiYong Sun'
__doc__ = '在排序数组中查找数字出现的次数' \
          '1--最简单快速的办法是 二分解法一'

from typing import List
import bisect
import collections

class Solution_1:
    def search(self, nums: List[int], target: int) -> int:
        # 二分法 二
        size = len(nums)  # 实现bisect.bisect_left
        left, right = 0, size
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        first, second = 0, len(nums)  # 实现bisect.bisect_right
        while first < second:
            mid = first + (second - first) // 2
            if nums[mid] <= target:
                first = mid + 1
            else:
                second = mid
        return first - left

class Solution_2:
    def search(self, nums: List[int], target: int) -> int:
        # 二分法 一
        return bisect.bisect(nums, target) - bisect.bisect_left(nums, target)

class Solution_3:
    def search(self, nums: List[int], target: int) -> int:
        # 字典计数 三
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        return count[target] if target in count else 0

class Solution_4:
    def search(self, nums: List[int], target: int) -> int:
        # 字典计数 二
        count = collections.defaultdict(int)
        for num in nums:
            count[num] += 1
        return count[target]

class Solution_5:
    def search(self, nums: List[int], target: int) -> int:
        # 字典计数 一
        count = collections.Counter(nums)
        return count[target]


if __name__ == "__main__":
    nums = [2, 3, 3, 4, 4, 7, 7, 7, 9]
    targets = [1, 2, 3, 4, 5, 6, 7, 8, 10]

    for target in targets:
        print('1--', target, Solution_1().search(nums, target))
        print('2--', target, Solution_2().search(nums, target))
        print('3--', target, Solution_3().search(nums, target))
        print('4--', target, Solution_4().search(nums, target))
        print('5--', target, Solution_5().search(nums, target))