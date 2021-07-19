__time__ = '2021/7/19'
__author__ = 'ZhiYong Sun'

"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？


# 很明显是要使用深度有限搜索的， 另外这道题的难处在于numx，numy的迭代关系
# 机器人只会往下走和往右走
"""

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = set()    # 禁忌表

        def dfs(x, y, numx, numy):
            if not (0 <= x < m and 0 <= y < n) or numx + numy > k or (x, y) in visited:
                return False
            visited.add((x, y))
            return 1 + dfs(x + 1, y, numx + 1 if (x + 1) % 10 else numx - 8,  numy) + \
                   dfs(x, y + 1, numx, numy + 1 if (y + 1) % 10 else numy - 8)     # 机器人只会往下走和往右走
        return dfs(0, 0, 0, 0)


if __name__ == "__main__":
    m, n, k = 38, 28, 30
    print(Solution().movingCount(m, n, k))
