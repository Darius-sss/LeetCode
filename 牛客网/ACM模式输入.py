__time__ = '2021/7/24'
__author__ = 'ZhiYong Sun'

# 牛客网的ACM模式输入
"""
2
3
1 3 2
0 2 3
4
1 5 4 2 
10 32 19 21
"""

n = int(input())   # 一行一个数字
for _ in range(n):
    n = int(input())  # 一行一个数字
    X = list(map(int, input().split()))  # 一行多个数字
    Y = list(map(int, input().split()))  # 一行多个数字