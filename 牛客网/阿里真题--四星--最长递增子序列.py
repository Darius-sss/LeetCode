__time__ = '2021/7/24'
__author__ = 'ZhiYong Sun'
__doc__ = '动态规划或者二分法' \
          '二分法更快O(nlgn) 动态规划O(N^2)' \
          '这道题的本质在于寻找 最长有序子序列 '


"""
小强现在有个物品,每个物品有两种属性和.他想要从中挑出尽可能多的物品满足以下条件:对于任意两个物品和,满足或者.问最多能挑出多少物品.
"""

from bisect import bisect_left
T = int(input())
for _ in range(T):
    n = int(input())
    X = map(int, input().split())
    Y = map(int, input().split())
    a = sorted(zip(X, Y), key=lambda x: (x[0], -x[1]))   # 关键在于x相等时按照y降序
    total = 0
    q = [0] * 1000005
    for i in range(n):
        t = bisect_left(a=q, x=a[i][1], lo=0, hi=total)  # bisect_left(a, x, lo, hi)--a列表，x目标，lo下限，hi上限
        if t == total:
            total += 1
        q[t] = a[i][1]

    print(total)
