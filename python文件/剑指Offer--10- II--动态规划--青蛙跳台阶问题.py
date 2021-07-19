__time__ = '2021/7/18'
__author__ = 'ZhiYong Sun'

"""一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。"""

"""这题和斐波那契那题基本一致， 除了初始化时curr=1"""


class Solution:
    def numWays(self, n: int) -> int:
        curr, post = 1, 1
        for _ in range(n):
            curr, post = post, curr + post
        return curr


if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5, 6, 70]
    for n in nums:
        print(Solution().numWays(n))