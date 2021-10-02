__time__ = '2021/9/10'
__author__ = 'ZhiYong Sun'

"""
成绩上涨幅度

题目描述：
小程所在院系进行了期末考试。考试后小程发现老师登分产生了错误，遂寻找老师修改分数。
老师将小程的分数做了修正。现在小程想知道他的成绩上升了多少名。
注意：同分数的情况下，排名应该相同。比如说现在班里有五名同学，Alice 100分，Bob 90分， Cindy 80分， David 80分，Emily 70分
则他们的名次为
Alice 排名 1
Bob 排名2
Cindy 排名3
David 排名3
Emily 排名 5
之后把Cindy 的分数修改为100分，则此时Alice和Cindy都是第一名。
于是Cindy 的排名上升了 3 - 1 = 2名。
你的任务就是协助小程计算他名次上升了多少。
本题中保证小程修改分数后，不会出现名次下降的情况。

输入描述
第一行三个空格分隔开的正整数，分别表示学生数量n，小程原来的分数x，小程修改后的分数y。保证 y >= x
接下来n个空格分隔开的正整数表示原先n个同学的分数。其中包括小程原来的分数，换句话说，这一行除了描述了小程成绩之外，还描述了另外n-1个同学的成绩。
成绩的给出顺序不保证有序。
输出描述
输出小程修改后的名次上涨幅度。

样例输入
5 80 100
100 90 80 80 70
样例输出
2
提示
1<= n <= 100000，小程原来的分数x和修改后的分数y有1<= x, y <= 1000，且保证y >= x。

"""

n, x, y = list(map(int, input().split()))
grades = list(map(int, input().split()))

grades.sort()
old, new = 0, 0

for ind, num in enumerate(grades):
    if num <= y:
        new = ind
    if num == x:
        old = ind
print(new-old)

"""
福利发放

题目描述：
现在小程在运营一个游戏，游戏需要向含有特定关键词的用户发放惊喜福利。
现在给定你所有用户的用户名和需要检测的关键词。
你的任务是反馈给运营，本次发放会发放福利给多少名用户。
用户名仅含有大小写字母和数字。关键词仅包含字母，且关键词检测不区分大小写。

输入描述
第一行一个正整数n表示游戏有n个用户，一个字符串s表示需要检测的关键词。中间有空格隔开。
接下来n行每行一个字符串，为n个用户名。

输出描述
一行一个正整数表示本次发放会发放福利给多少名用户。

样例输入
4 hAppy
happy01
bad02
happ03
hAPPY66
样例输出
2

提示
第一个用户happy01和第四个用户hAPPY66将获得福利。
保证所有的字符串仅包含大小写字符和数字，长度不超过30

1 <= n <= 500

"""
n, S = input().split()
n = int(n)
S = S.lower()
count = 0
for _ in range(n):
    str = input().lower()
    if S in str:
        count += 1
print(count)

"""
仓储调动

题目描述：
小程现在协助管理一个大型仓库。其中有非常多的货物。
现在来了很多运货车。每辆车只能装载一件货物，毫无疑问从经济的角度而言应该尽可能让这辆车满载。
当然，也可能出现这辆车无法承载货物的可能。例如如果此时仓库最轻货物是重量100的，而这辆车的承载能力是50，那无论如何都无法使得这辆车运输货物。
小程现在的打算是，每当一辆车过来，就尽量使得它满载。（注：满载允许货物重量等于承载能力，即若承载能力是50，可以载重重量为50的货物）
请注意：车是依次过来的，小程并不能事先预知所有的车的承载能力，只能尽量满足当前车。
你的任务是求出小程每次为这些车所选择的货物重量。


输入描述
第一行两个正整数n,m，分别表示仓库中的货物数量和前来的运货车数量。
第二行n组数据，表示n个货物的自身重量，以空格分隔。数据不保证有序。
第三行m组数据，按顺序给出每次前来的运货车的承载能力。

注意，数字间均有空格隔开。

输出描述
对于每个运货车，输出它所承载的货物重量；若这辆运货车无货可载，输出-1。每个输出之间以一个空格作为分隔。

样例输入
5 6
5 10 5 11 10
10 10 1 5 4 6
样例输出
10 10 -1 5 -1 5
提示
输入样例2
10 10
5 6 4 9 1 7 7 5 8 1
2 2 3 7 2 8 4 1 9 3

输出样例2
1 1 -1 7 -1 8 4 -1 9 -1
1<=n,m<=100,000，货物和载重范围在[1, 200]之间
"""
def check(target):
    if not nums or target < nums[-1]:
        return False
    dp = [False] * (target + 1)
    dp[0] = True
    status = []
    for num in nums:
        if num <= target:
            for j in range(target, num-1, -1):
                dp[j] = dp[j] or dp[j - num]
        status.append(dp[:])
        if dp[-1]:
            return status
    return status

def pick(status, target):
    if not status:
        return (-1, [])
    mx_weight = 0
    for i in range(target, -1, -1):
        if status[-1][i]:
            mx_weight = i
            break
    tmp = mx_weight
    ans = []
    while tmp != 0:
        for i in range(len(status)):
            if status[i][tmp]:
                ans.append(nums[i])
                tmp -= nums[i]
                break
    return (mx_weight, ans)


n, m = list(map(int, input().split()))
nums = list(map(int, input().split()))
cars = list(map(int, input().split()))
res = []
nums.sort(reverse=True)
for target in cars:
    status = check(target)
    mx, goods = pick(status, target)
    print(goods)
    res.append(mx)
    for num in goods:
        nums.remove(num)

print(' '.join(list(map(str, res))))



