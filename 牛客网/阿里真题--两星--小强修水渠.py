__time__ = '2021/7/30'
__author__ = 'ZhiYong Sun'

"""
在一张地图上小强有座房子,因为地理位置的原因没有办法给每座房子提供水源,所以小强打算修建一条平行轴的水渠.

因为这条水渠无限长.所以能够看做是一条平行于轴的直线. 

现在小强想确定修建水渠的位置,能够使得这座房子到水渠的垂直距离和最小,请你输出最小的距离和.
"""

n = int(input())
x, y = [], []

for _ in range(n):
    nums = list(map(int, input().split()))
    x.append(nums[0])
    y.append(nums[1])

index = sorted(x)[n // 2]
ans = 0
for k in x:
    ans += abs(k - index)

print(ans)

"""
input:
4
0 0
0 50
100 50
50 0
"""