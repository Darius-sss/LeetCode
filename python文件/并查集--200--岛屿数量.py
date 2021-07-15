__time__ = '2021/7/3'
__author__ = 'ZhiYong Sun'

class UnionFind:
    # 并查集 数据结构
    # 并查集优化：union by rank
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rooty] > self.rank[rootx]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1


class Solution:

    def numIsLands(self, grid):
        if not grid or not grid[0]: return 0
        uf = UnionFind(grid)
        dx = [1, 0]
        dy = [0, 1]
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                for k in range(2):
                    x, y = i + dx[k], j + dy[k]
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                        uf.union(i*n+j, x*n+y)
        print(uf.count)
        return uf.count



if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "1"],
        ["1", "1", "1", "0", "0"],
        ["1", "0", "1", "0", "1"]
    ]

    Solution().numIsLands(grid)