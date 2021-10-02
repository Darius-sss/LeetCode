__time__ = '2021/8/25'
__author__ = 'ZhiYong Sun'

'''将数组按照大小顺序转换成序号数组'''
nums = input()[1:-1].split(',')
nums = list(map(int, nums))
n = len(nums)
raw_index = list(range(n))
data = list(map(list, zip(nums, raw_index)))
data.sort(key=lambda x: (x[0], x[1]))

tmp = data[0][0]
data[0][0] = 1
for i in range(1, n):
    if data[i][0] == tmp:
        data[i][0] = data[i-1][0]
    else:
        data[i][0] = data[i-1][0] + 1
        tmp = data[i][0]
data.sort(key=lambda x: x[1])
res = list(list(zip(*data))[0])
res = list(map(str, res))
print('['+','.join(res)+']')



'''F(n) = F(n-2) + F(n-3)'''
n = int(input())
if n <= 3:
    print('1')
else:
    one, two, three = 1, 1, 1
    for _ in range(n-3):
        one, two, three = two, three, one + two

    print(str(three))

'''罗马数字转整数'''
S = input()
n = len(S)
hashmap1 = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
hashmap2 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
ans = 0
for i in range(n - 2, -1, -1):
    ch = S[i:i + 2]
    if ch in hashmap1:
        ans += hashmap1[ch]
        S = S[0:i] + S[i + 2:]
for ch in S:
    ans += hashmap2[ch]

print(ans)


