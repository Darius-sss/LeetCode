__time__ = '2021/7/20'
__author__ = 'ZhiYong Sun'

"""
编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为 汉明重量).）。
"""


class Solution:        # n & n - 1 --  二进制数1好帮手
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n-1
            count += 1
        return count


if __name__ == "__main__":
    n = 11
    print(Solution().hammingWeight(n))

    n = 128
    print(Solution().hammingWeight(n))