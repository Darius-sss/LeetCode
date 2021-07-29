__time__ = '2021/7/28'
__author__ = 'ZhiYong Sun'


"""
编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += 1
            n &= n-1
        return count


if __name__ == "__main__":
    nums = [1, 2, 3, 6]
    for num in nums:
        print(Solution().hammingWeight(num))




