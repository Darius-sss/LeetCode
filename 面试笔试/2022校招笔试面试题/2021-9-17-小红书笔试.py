__time__ = '2021/9/18'
__author__ = 'ZhiYong Sun'

"""
遥控机器人
题目描述：
薯队长买了获得了一个遥控机器人。机器人可以接受三种指令： 向前走几步，向左转90度，向右转90度。
这一代的机器上还不具备跨越障碍的能力。机器人在向前的过程中如果遇到障碍或者试图走出边界，则会自动停下。
薯队长把机器人放在一个有障碍的有界网格上，并给机器人发指令。
你需要给出机器人最终所处的位置与初始位置之间的行和列的偏移量。

输入描述
3 6 // R行 C列，B是空地，O是障碍，R是机器人（初始朝向向上），  1<= R, C <=100
BBBBBB
BRBOBB
BBBBOB

6 // 6条指令 , 指令数<=1000
Turn right // (2, 2) 朝右
Forward 3 // (2, 2) -> (2，3) 遇上障碍
Turn left // (2, 3) 朝上
Forward 2 // (1, 3) 遇上边界
Turn left // (1, 3) 朝左
Forward 1 // (1, 2)

输出描述
-1 0 // 行偏移和列偏移量

样例输入
3 6
BBBBBB
BRBOBB
BBBBOB
6
Turn right
Forward 3
Turn left
Forward 2
Turn left
Forward 1
样例输出
-1 0

提示
不用做输入格式检查

"""

m, n = list(map(int, input().split()))   # 行列数
start, cur = [], []   # 包含初始位置
flag = 0
stones = []   # 障碍物
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]    # 上右下左方向数组

for i in range(m):
    line = input()
    for j in range(n):
        if line[j] == 'R':
            start, cur = [i, j], [i, j]
        elif line[j] == 'O':
            stones.append([i, j])

count = int(input())   # 指令数目
for _ in range(count):
    code = input()
    if code == 'Turn left':
        flag = flag - 1 if flag > 0 else 3
    elif code == 'Turn right':
        flag = flag + 1 if flag < 3 else 0
    else:
        step = int(code.split()[1])
        for _ in range(step):
            cur_x, cur_y = cur[0]+dx[flag], cur[1]+dy[flag]
            if [cur_x, cur_y] in stones or not (0<= cur_x <= m-1 and 0<= cur_y <= n-1):
                break
            else:
                cur[0], cur[1] = cur_x, cur_y

print(cur[0]-start[0], cur[1]-start[1])


"""
漂亮数组

题目描述：
有一个包含 n 个   不相同   整数的数组 arr = [a[0], a[1], ..., a[n-1]]。 你可以随意交换数组中的任意两个元素的位置。
一个数组如果满足 在0<i<n 区间 |arr[i] - arr[i-1]| （绝对值）的和最小，则称这个数组为漂亮数组。
给到一个数组 arr , 计算并返回需要交换的最小次数，使得数组 arr 变为一个漂亮数组。

样例
arr = [7, 15, 12, 3]
arr 对应的一种漂亮数组为[3, 7, 12, 15]. 为了变换成这样的数组，需要做如下交换操作
    Swap      Result             [7, 15, 12, 3]     3 7   [3, 15, 12, 7]     7 15  [3, 7, 12, 15]

共执行2次元素交换操作使得输入数组变换成漂亮数组，这是所需要的最少交换次数。

输入描述
第一行输入是一个整数 n, 标识输入数组的元素个数. 第二行输入包含n个用空格分割的整数arr[i]

输出描述
最小需要进行交换的次数

样例输入
4
2 5 3 1
样例输出
2
"""
n = int(input())
nums = list(map(int, input().split()))
index = list(range(n))
lt = [index, nums]
lt = list(zip(*lt))
lt_up = sorted(lt, key=lambda x: x[1])
lt_down = sorted(lt, key=lambda x: -x[1])

ind_up = [x[0] for x in lt_up]
ind_down = [x[0] for x in lt_down]


def check(ind):
    res = 0
    visited = set()
    for num in index:
        if num in visited:
            break
        visited.add(num)
        tmp = [num]
        while tmp:
            cur = tmp[-1]
            if len(tmp)== 1 and ind[cur] == num:
                break
            if ind[cur] in tmp:
                old_id = tmp.index(ind[cur])
                res += len(tmp)-old_id-1
                tmp = tmp[:old_id]
            else:
                tmp.append(ind[cur])
                visited.add(ind[cur])
    return res

print(min(check(ind_up), check(ind_down)))


"""
押韵诗
题目描述：
薯队长最近迷上了写一种抽象诗，由于诗歌的意义对于抽象诗意义不大，薯队长想用非同寻常的词语组合打动读者。现在，他为未来的诗歌准备了N行诗句，不过他突然意识到这些诗并不押韵。
薯队长决定遵循古诗的押韵。诗歌被分为若干段，每段都是四行诗。每一句诗都有一个韵脚，假如A和B表示两种不同的韵脚，
每段四行诗的韵脚只可能是 “AABB”, “ABAB”, “ABBA” 和“AAAA”中的一种。
薯队长现状将诗句的韵脚都编了号，具有相同编号的句子代表有相同的韵脚。现在，薯队长想删掉一些句子，使得剩下的都是遵循押韵规则的四行诗。
请帮薯队长找出满足条件最长的诗歌。当然了，是不能改变诗句的顺序的。

输入描述
数据第一行包括整数N(1<=N<=4000)，代表诗歌的句子数。
接下来N个整数分别表示每一行诗的韵脚。这些数字都是不超过10^9的正数。

输出描述
一行一个整数k，为薯队长最多能够得到的四行诗个数。

样例输入
15
1 2 3 1 2 1 2 3 3 2 1 1 3 2 2
样例输出
3

提示
样例分成三段四行诗，分别为：

1 2 4 5

7 8 9 10

11 12 14 15

"""


