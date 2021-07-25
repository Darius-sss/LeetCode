__time__ = '2021/7/23'
__author__ = 'ZhiYong Sun'
__doc__ = '深度搜索DFS'

"""
有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。

给你一个坐标(sr, sc)表示图像渲染开始的像素值（行 ，列）和一个新的颜色值newColor，让你重新上色这幅图像。

为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，

接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。

最后返回经过上色渲染后的图像。

"""

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])   # 行列
        visited = set()   # 禁忌表
        dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)  # 方向数组 -- 上下左右
        color = image[sr][sc]

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or image[x][y] != color or (x, y) in visited: return False

            image[x][y] = newColor
            visited.add((x, y))

            for k in range(4):
                dfs(x + dx[k], y + dy[k])

        dfs(sr, sc)
        return image


if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    print(Solution().floodFill(image, sr, sc, newColor))

    image = [[0, 0, 0], [0, 0, 0]]
    sr = 0
    sc = 0
    newColor = 2
    print(Solution().floodFill(image, sr, sc, newColor))

