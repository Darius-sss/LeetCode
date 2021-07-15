__time__ = '2021/7/4'
__author__ = 'ZhiYong Sun'


"""
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

"""


from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 状态初始化
        m, n = len(triangle), len(triangle[-1])
        dp = [[float('inf')] * m for _ in range(n)]
        dp[0][0] = triangle[0][0]

        # 状态转移
        for i in range(1, m):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1]+triangle[i][j], dp[i-1][j]+triangle[i][j])

        print(dp)
        print(min(dp[-1]))
        return int(min(dp[-1]))


class Solution_two:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 从下往上进行状态转移

        dp = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        print(dp[0])
        return dp[0]


if __name__ == "__main__":
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    Solution().minimumTotal(triangle)
    Solution_two().minimumTotal(triangle)