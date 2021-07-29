__time__ = '2021/7/29'
__author__ = 'ZhiYong Sun'
__doc__ = '完全背包问题'

from typing import List

"""
给你一个整数数组 coins 表示不同面额的硬币，另给一个整数 amount 表示总金额。

请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 0 。

假设每一种面额的硬币有无限个。

题目数据保证结果符合 32 位带符号整数。
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:   # 以硬币coin结尾
            for x in range(coin, amount + 1):   # x比coin大才可以从coin转换过来
                dp[x] += dp[x-coin]    # dp[x]表示到x的组合数
        return dp[amount]


if __name__ == "__main__":
    amount = 5
    coins = [1, 2, 5]
    print(Solution().change(amount, coins))