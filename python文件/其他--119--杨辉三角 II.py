__time__ = '2021/7/30'
__author__ = 'ZhiYong Sun'

from typing import List

"""
给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。
"""


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 通项公式
        arr = [1] * (rowIndex + 1)
        for i in range(1, len(arr) - 1):
            arr[i] = arr[i - 1] * (rowIndex - i + 1) // i  # 通向
        return arr


class Solution_:
    def getRow(self, rowIndex: int) -> List[int]:
        # 滚动数组
        # 可以从后往前，这样不需要辅助数组
        res = [1]

        for _ in range(rowIndex):
            tmp = res[:]
            for i in range(1, len(res)):
                res[i] = tmp[i] + tmp[i - 1]
            res.append(1)

        return res


if __name__ == "__main__":
    nums = list(range(1, 8))
    for n in nums:
        print(Solution().getRow(n))
        print(Solution_().getRow(n))