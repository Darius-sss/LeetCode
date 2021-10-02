__time__ = '2021/8/22'
__author__ = 'ZhiYong Sun'

from typing import List

"""
你在进行一个简化版的吃豆人游戏。你从 [0, 0] 点开始出发，你的目的地是target = [xtarget, ytarget] 。

地图上有一些阻碍者，以数组 ghosts 给出，第 i 个阻碍者从ghosts[i] = [xi, yi]出发。所有输入均为 整数坐标 。

每一回合，你和阻碍者们可以同时向东，西，南，北四个方向移动，每次可以移动到距离原位置 1 个单位 的新位置。当然，也可以选择 不动 。所有动作 同时 发生。

如果你可以在任何阻碍者抓住你 之前 到达目的地（阻碍者可以采取任意行动方式），则被视为逃脱成功。如果你和阻碍者同时到达了一个位置（包括目的地）都不算是逃脱成功。

只有在你有可能成功逃脱时，输出 true ；否则，输出 false 。

"""

"""求解思路： 如果有阻碍者可以在我之前到达终点，则逃脱失败"""


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        mn = float('inf')
        for i, j in ghosts:
            mn = min(mn, abs(i-target[0]) + abs(j-target[1]))
        if mn <= abs(target[0]) + abs(target[1]):
            return False
        return True


if __name__ == "__main__":
    ghosts = [[1, 9], [2, -5], [3, 8], [9, 8], [-1, 3]]
    target = [8, -10]

    print(Solution().escapeGhosts(ghosts, target))
