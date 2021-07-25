__time__ = '2021/7/24'
__author__ = 'ZhiYong Sun'
__doc__ = '广度优先搜索' \
          '这题和542--01矩阵大致类似'

"""

在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
"""
from typing import List
import collections


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        time = [[0] * n for _ in range(m)]   # 记录每个点橘子坏掉所需要的时间
        bad = [(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2]# 坏橘子的位置
        queue = collections.deque(bad)     # 申请一个队列
        taboo = set(bad)      # 申请一个集合放置搜索过的位置，即禁忌表

        while queue:  # 模拟橘子的感染过程
            i, j = queue.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in taboo and grid[ni][nj] == 1:
                    time[ni][nj] = time[i][j] + 1
                    queue.append((ni, nj))
                    taboo.add((ni, nj))

        for i in range(m):   # 如果原来是好橘子，但是time矩阵对应位置是0，则说明没有感染到该橘子，返回-1
            for j in range(n):
                if grid[i][j] == 1 and time[i][j] == 0:
                    return -1

        return max([max(nums) for nums in time])


if __name__ == "__main__":
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(Solution().orangesRotting(grid))

    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print(Solution().orangesRotting(grid))

    grid = [[0, 2]]
    print(Solution().orangesRotting(grid))
