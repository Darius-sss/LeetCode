__time__ = '2021/7/18'
__author__ = 'ZhiYong Sun'



from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        hashset = set()
        for num in nums:
            if num in hashset:
                return num
            hashset.add(num)


if __name__ == "__main__":
    nums = [2, 3, 1, 0, 2, 5, 3]
    print(Solution().findRepeatNumber(nums))
