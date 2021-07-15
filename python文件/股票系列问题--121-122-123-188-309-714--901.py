__time__ = '2021/7/4'
__author__ = 'ZhiYong Sun'
__doc__ = '动态规划DP--121-122-123-188-309-714--901--股票系列问题' \
          '前提--在持有股票时只能卖出不能买进' \
          '121--只能买卖一次' \
          '122--不限制买卖次数' \
          '123--最多只能买卖两次' \
          '188--最多只能买卖K次' \
          '309--卖完之后有一天冻结期不可操作' \
          '714--买股票需要支出手续费' \
          '901--股票价格跨度，即求连涨的跨度，自身为1--使用单调栈'


from typing import List


class Solution_121:
    # 只考虑手中的钱最多，买相当于减，卖相当于加，这一次是买还是卖只与上一次是买还是卖有关
    # 整体属于dp思想，对于第i价格，利润与之前价格都有关系，所以需要buy = max(buy, ？)，sell = max(sell, ？)
    # 即dp滚动数组思想，这意味着，我们每天（第i天为结尾）都在买卖（dp就是循环推导）
    def maxProfit(self, prices: List[int]) -> int:
        # 买卖一次
        buy, sell = -float('inf'), 0  # buy一定初始化为无穷小，因为第一次买看成手中钱减少（是个负数），sell初始化小于等于0
        for p in prices:
            buy = max(buy, 0-p)  # 由于只能买一次，买之前手里只有0元，买之后手里有max(buy, 0-p)
            sell = max(sell, buy+p)  # 卖之前一定是买buy，卖完手里有max(sell, buy+p)
        return sell


class Solution_122:
    def maxProfit(self, prices: List[int]) -> int:
        # 不限制买卖次数
        buy, sell = -float('inf'), 0
        for p in prices:
            buy = max(buy, sell-p)  # 由于不限制交易次数，买之前可能是卖过手里的钱sell，买之后max(buy, sell-p)
            sell = max(sell, buy+p)  # 卖之前一定是买buy，卖完手里有max(sell, buy+p)
        return sell


class Solution_123:
    def maxProfit(self, prices: List[int]) -> int:
        # 最多买卖两次
        buy1, sell1, buy2, sell2 = -float('inf'), 0, -float('inf'), 0
        for p in prices:
            buy1 = max(buy1, 0-p)
            sell1 = max(sell1, buy1+p)
            buy2 = max(buy2, sell1-p)
            sell2 = max(sell2, buy2+p)  # 整体而言，这次操作只与上一次有关
        return sell2


class Solution_188:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 最多买卖k次
        buy = [-float('inf')] * (k+1)
        sell = [0] * (k+1)  # 初始化为k+1，是因为第一次买，是0-p，这里我们sell[0]=0，就可以了
        for p in prices:
            for k in range(1, k+1):
                buy[k] = max(buy[k], sell[k-1]-p)  # 第一次sell[i-1]=sell[0]=0
                sell[k] = max(sell[k], int(buy[k]+p))
        return sell[-1]


class Solution_309:
    def maxProfit(self, prices: List[int]) -> int:
        # 不限制买卖次数，冻结期为1天
        buy, sell_pre, sell_now = -float('inf'), 0, 0
        # 冻结期为1天，意味着，我们买的上一个状态不能是上一次卖的，而是上上次卖的
        # 至此，要理解，这是dp滚动数组思想，这意味着，我们每天都在买卖
        for p in prices:
            buy = max(buy, sell_pre-p)  # 这次买的是接着上上次卖的，可以理解为buy[i]与sell[j-1]有关，而不是sell[j]
            sell_pre = sell_now  # 因为后面要更新sell_now，这里要先保存，sell[i-1]的记录
            sell_now = max(sell_now, buy+p)
        return sell_now


class Solution_714:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 不限制买卖次数，但是有手续费
        buy, sell = -float('inf'), 0
        for p in prices:
            buy = max(buy, sell-fee-p)  # 多减去手续费即可
            sell = max(sell, buy+p)
        return sell


class StockSpanner_901:

    def __init__(self):
        self.stack = [(float('inf'), 0)]
        self.count = 0

    def next(self, price: int) -> int:
        self.count += 1
        while price >= self.stack[-1][0]:
            self.stack.pop()
        self.stack.append((price, self.count))
        return self.count - self.stack[-2][-1]


if __name__ == "__main__":
    prices = [7, 2, 6, 1, 6, 4, 8, 9, 18, 3, 5, 7, 4, 7]
    res_121 = Solution_121().maxProfit(prices)
    print('只买卖一次的最大收益：', res_121)

    res_122 = Solution_122().maxProfit(prices)
    print('不限制买卖次数的最大收益：', res_122)

    res_123 = Solution_123().maxProfit(prices)
    print('最多买卖两次的最大收益：', res_123)

    res_188 = Solution_188().maxProfit(4, prices)
    print('最多买卖K(4)次的最大收益：', res_188)

    res_309 = Solution_309().maxProfit(prices)
    print('需要一天冻结期的最大收益：', res_309)

    res_714 = Solution_714().maxProfit(prices, 1)
    print('交易需要手续费(1)的最大收益：', res_714)

    nums_901 = [100, 80, 60, 70, 60, 75, 85]
    Solution = StockSpanner_901()
    res_901 = []
    for num in nums_901:
        res_901.append(Solution.next(num))
    print(res_901)