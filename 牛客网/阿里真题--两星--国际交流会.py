__time__ = '2021/7/30'
__author__ = 'ZhiYong Sun'


"""
最近小强主办了一场国际交流会，大家在会上以一个圆桌围坐在一起。由于大会的目的就是让不同国家的人感受一下不同的异域气息，为了更好地达到这个目的，

小强希望最大化邻座两人之间的差异程度和。为此，他找到了你，希望你能给他安排一下座位，达到邻座之间的差异之和最大。
"""

n = int(input())
nums = list(map(int, input().split()))

nums.sort()
i, j = 0, n-1
res = []
while i <= j:
    res.append(nums[i])
    i += 1
    if i < j:
        res.append(nums[j])
        j -= 1

ans = abs(res[0]-res[-1])
for k in range(1, n):
    ans += abs(res[k] - res[k-1])
print(ans)
print(' '.join(list(map(str, res))))


"""
4
3 6 2 9
"""


