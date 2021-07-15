__time__ = '2021/7/11'
__author__ = 'ZhiYong Sun'

from typing import List

"""
给定一位研究者论文被引用次数的数组（被引用次数是非负整数）。编写一个方法，计算出研究者的 h 指数。

h 指数的定义：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。且其余的 N - h 篇论文每篇被引用次数 不超过 h 次。

例如：某人的 h 指数是 20，这表示他已发表的论文中，每篇被引用了至少 20 次的论文总共有 20 篇。

"""


class Solution_two:    # 排序 + 二分法
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        size = len(citations)
        left, right = 0, size-1
        while left <= right:

            mid = (left + right) >> 1
            if citations[mid] < mid+1:
                right = mid - 1
            else:
                left = mid + 1
        return left


class Solution:    # 排序 + 遍历
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for ind, num in enumerate(citations):
            if num < ind+1:
                return ind

        return len(citations)


if __name__ == "__main__":
    citations = [1, 2, 1, 6, 7, 0]
    res1 = Solution().hIndex(citations)
    print(res1)
    res2 = Solution_two().hIndex(citations)

    print(res2)