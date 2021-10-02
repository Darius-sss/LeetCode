__time__ = '2021/8/8'
__author__ = 'ZhiYong Sun'



""" 美团笔试 2021-8-8 10:00--12:00"""

"""
一：
小美和小团在玩游戏。小美将会给出n个大小在1到n之间（包括1和n）的整数，然后小美会再告诉小团一个整数k，小团需要找到一个最小的整数x满足以下条件：

整数x的大小在1到n之间（包括1和n）

在小美给出的n个整数中，恰好有k个数严格比x小

2
6 1
1 6 6 2 1 3
6 3
1 6 5 2 2 5
"""

# T = int(input())
#
# for _ in range(T):
#     n, k = list(map(int, input().split()))
#     data = list(map(int, input().split()))
#     data.sort()
#     if k == 0:
#         print('YES')
#         print(data[0])
#     elif k > 0 and data[k-1] < n and data[k] > data[k-1]:
#         print('YES')
#         print(data[k-1]+1)
#     else:
#         print('NO')


"""
二：
一个53键的坏键盘，其中有26个小写字母 26个大写字母 一个空格

每次按下可能会重复多次

规定：连续输入的两个字符不一致，并且不输入空格

将给定的字符串回归为该有的样子

‘i sss HH h sss GGGikh    ’

"""

# strs = input()
# strs = strs.replace(' ', '')
# chs = list(strs)
# for i in range(len(chs)-1, 0, -1):
#     if chs[i] == chs[i-1]:
#         del chs[i]
# print(''.join(chs))


"""
三：
给定一个数组，在每个数的前面找到比这个树小的最大数...

5
1 6 3 3 8
"""


mn_stack, mx_stack = [], []
n = int(input())
nums = list(map(int, input().split()))
mn_stack.append(nums[0])
res = [0]

for i in range(1, n):
    while mn_stack and nums[i] <= mn_stack[-1]:
        mx_stack.append(mn_stack.pop())
    while mx_stack and nums[i] > mx_stack[-1]:
        mn_stack.append(mx_stack.pop())
    if not mn_stack:
        res.append(0)
    else:
        res.append(mn_stack[-1])
    mn_stack.append(nums[i])

ans = 0
for i in range(1, n+1):
    ans += i * res[i-1]
print(ans)


n = int(input())
nums = list(map(int, input().split()))

data = [nums, list(range(1, n + 1))]
data = list(map(list, zip(*data)))
data.sort(key=lambda x: (x[0], -x[1]))

res = [0]
for i in range(1, n):
    tmp = i - 1
    while tmp >= 0:
        if data[i][0] > data[tmp][0] and data[i][1] > data[tmp][1]:
            res.append(data[tmp][0])
            break
        else:
            tmp -= 1
        if tmp < 0:
            res.append(0)
            break
ans = 0
for i in range(n):
    ans += data[i][1] * res[i]
print(ans)


"""
给定一个偶数个数字的数组，求最小操作次数使得前后两部分完全一致

操作方法为：选定一个数字将所有该数字都变成另外一个数字
"""

"""代码给忘了..."""
