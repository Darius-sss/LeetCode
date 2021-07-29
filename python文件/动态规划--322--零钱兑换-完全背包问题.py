__time__ = '2021/7/29'
__author__ = 'ZhiYong Sun'

from typing import List

"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回-1 。

你可以认为每种硬币的数量是无限的。
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):   # x比coin大才可以从coin转换过来
                dp[x] = min(dp[x], dp[x-coin] + 1)   # dp[x]表示到x的最少硬币数量，要么是之前的，要么是更新后的即dp[x-coin]+1
        return dp[amount]


if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 11
    print(Solution().coinChange(coins, amount))