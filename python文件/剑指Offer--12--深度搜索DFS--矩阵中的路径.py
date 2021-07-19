__time__ = '2021/7/19'
__author__ = 'ZhiYong Sun'


"""
给定一个m x n 二维字符网格board 和一个字符串单词word 。如果word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。

同一个单元格内的字母不允许被重复使用。

"""

from typing import List


class Solution:  # 直接在原数组上修改
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(x, y, k):
            if not (0 <= x < m and 0 <= y < n) or board[x][y] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            board[x][y] = '#'
            res = dfs(x - 1, y, k + 1) or dfs(x + 1, y, k + 1) or dfs(x, y - 1, k + 1) or dfs(x, y + 1, k + 1)
            board[x][y] = word[k]
            return res

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False


class Solution_two:  # 添加禁忌表visited；这里的禁忌表是局部变量
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(visited, i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or (i, j) in visited or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            res = dfs(visited+[(i, j)], i + 1, j, k + 1) or dfs(visited+[(i, j)], i - 1, j, k + 1) \
                  or dfs(visited+[(i, j)], i, j + 1, k + 1) or dfs(visited+[(i, j)], i, j - 1, k + 1)
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs([], i, j, 0):
                    return True
        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(Solution().exist(board, word))

    board1 = [["a", "b"]]
    word1 = "ba"
    print(Solution().exist(board1, word1))

    board2 = [["a"]]
    word2 = "a"
    print(Solution().exist(board2, word2))

    board3 = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    word3 = "AAB"
    print(Solution().exist(board3, word3))

    board4 = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    word4 = "ABCESEEEFS"
    print(Solution().exist(board4, word4))