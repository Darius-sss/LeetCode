__time__ = '2021/7/3'
__author__ = 'ZhiYong Sun'


class Solution:

    def __init__(self, grid):
        self.grid = grid   # 岛屿排列情况
        self.dx = [-1, 1, 0, 0]   # dx dy 形成上下左右 方向数组
        self.dy = [0, 0, -1, 1]
        self.row = len(grid)     # 岛屿宽
        self.col = len(grid[0])     # 岛屿长
        self.visited = set()     # 记录已判断过的岛屿
        self.count = 0

    def numIslands(self):
        if not grid or not grid[0]: return 0
        self.count = sum([self._dfs(i, j) for i in range(self.row) for j in range(self.col)])
        # print(self.count)
        return self.count

    def _is_valid(self, x, y):
        # 判断位置的是否是岛屿
        if x < 0 or x >= self.row or y < 0 or y >= self.col:
            return False
        if self.grid[x][y] == '0' or ((x, y) in self.visited):
            return False
        return True

    def _dfs(self, x, y):
        if not self._is_valid(x, y):
            return 0
        self.visited.add((x, y))
        for k in range(4):
            self._dfs(x + self.dx[k], y + self.dy[k])
        return 1


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    Solution(grid=grid).numIslands()


