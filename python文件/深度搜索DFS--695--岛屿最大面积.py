__time__ = '2021/7/23'
__author__ = 'ZhiYong Sun'

"""
给定一个包含了一些 0 和 1 的非空二维数组grid 。

一个岛屿是由一些相邻的1(代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设grid 的四个边缘都被 0（代表水）包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)

"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])   # 行列
        dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] == 0:   # 条件
                return False
            grid[x][y] = 0      # 搜索过的地方标记为0
            count = 1                # 初始面积为1（当前不为0）
            for k in range(4):
                count += dfs(x + dx[k], y + dy[k])
            return count

        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
        return ans


if __name__ == "__main__":
    grid = [[1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(Solution().maxAreaOfIsland(grid))

