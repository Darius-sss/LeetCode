__time__ = '2021/7/23'
__author__ = 'ZhiYong Sun'
__doc__ = '广度优先搜索'

"""
给定一个由 0 和 1 组成的矩阵 mat，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

"""
from typing import List
import collections


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dist = [[0] * n for _ in range(m)]  # 记录的距离矩阵
        zeros = [(i, j) for i in range(m) for j in range(n) if mat[i][j] == 0]  # 所有 0 存在的位置
        queue = collections.deque(zeros)  # 申请一个队列， 将一开始出现0的位置都添加到队列中
        taboo = set(zeros)  # 创建一个禁忌表，如果搜索过的则不在搜索

        while queue:
            i, j = queue.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), [i, j - 1], (i, j + 1)]:  # 对周边（上下左右）进行搜索
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in taboo:  # 条件
                    dist[ni][nj] = dist[i][j] + 1  # 如果满足条件， 则距离加1
                    queue.append((ni, nj))  # 添加到队列当中
                    taboo.add((ni, nj))  # 添加到禁忌表中

        return dist


if __name__ == "__main__":
    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    print(Solution().updateMatrix(mat))