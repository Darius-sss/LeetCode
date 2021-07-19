__time__ = '2021/7/18'
__author__ = 'ZhiYong Sun'

"""
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。

请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

解题思路： 从左下角开始，如果比左下角大则往右走，否则往上走
"""

from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        m, n = len(matrix), len(matrix[0])

        i, j = m-1, 0
        while 0 <= i < m and 0 <= j < n:
            curr = matrix[i][j]
            if target == curr:
                return True
            elif target > curr:
                j += 1
            else:
                i -= 1
        return False


if __name__ == "__main__":
    matrix = [
              [1,   4,  7, 11, 15],
              [2,   5,  8, 12, 19],
              [3,   6,  9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]
            ]
    print(Solution().findNumberIn2DArray(matrix=matrix, target=19))
    print(Solution().findNumberIn2DArray(matrix=matrix, target=29))

