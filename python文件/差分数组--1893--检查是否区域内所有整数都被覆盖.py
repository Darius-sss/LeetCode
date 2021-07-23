__time__ = '2021/7/23'
__author__ = 'ZhiYong Sun'
__doc__ = '差分数组标准解法'


"""
给你一个二维整数数组ranges和两个整数left和right。每个ranges[i] = [starti, endi]表示一个从starti到endi的闭区间。

如果闭区间[left, right]内每个整数都被ranges中至少一个区间覆盖，那么请你返回true，否则返回false。

已知区间 ranges[i] = [starti, endi] ，如果整数 x 满足 starti <= x <= endi，那么我们称整数x被覆盖了。

"""
from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52
        for l, r in ranges:
            diff[l] += 1
            diff[r + 1] -= 1

        curr = 0
        for i in range(1, 51):
            curr += diff[i]
            if left <= i <= right and curr <= 0:
                return False
        return True


if __name__ == "__main__":
    ranges = [[1, 2], [3, 4], [5, 6]]
    left = 2
    right = 5
    print(Solution().isCovered(ranges, left, right))

    ranges = [[1, 10], [10, 20]]
    left = 21
    right = 21
    print(Solution().isCovered(ranges, left, right))