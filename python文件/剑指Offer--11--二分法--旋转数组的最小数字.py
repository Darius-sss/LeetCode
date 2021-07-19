__time__ = '2021/7/19'
__author__ = 'ZhiYong Sun'

"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。

例如，数组[3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

"""

from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left, right = 0, len(numbers)-1

        while left < right:
            mid = left + right >> 1

            if numbers[mid] > numbers[right]:   # mid比最右边的值还要大，则说明最小值在mid后面
                left = mid + 1
            elif numbers[mid] < numbers[left]:  # mid比最左边的值还要小，则说明最小值在mid前面
                right = mid
            else:
                right -= 1
        return numbers[left]


class Solution_two:
    def search(self, numbers):
        res = numbers[0]
        for num in numbers:
            if num < res:
                return num
        return res


if __name__ == "__main__":
    numbers = [3, 4, 5, 1, 2]
    print(min(numbers))
    print(Solution().minArray(numbers))
    print(Solution_two().search(numbers))


