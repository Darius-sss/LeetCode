__time__ = '2021/7/18'
__author__ = 'ZhiYong Sun'
__doc__ = '斐波那契数列'


class Solution:
    def fib(self, n: int) -> int:
        curr, post = 0, 1
        for _ in range(n):
            curr, post = post, curr + post
        return curr


if __name__ == "__main__":
    nums = [0, 1, 2, 3, 5, 9, 10, 82]
    for num in nums:
        print(Solution().fib(num))