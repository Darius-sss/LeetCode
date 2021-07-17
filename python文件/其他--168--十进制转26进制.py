__time__ = '2021/7/17'
__author__ = 'ZhiYong Sun'
__doc__ = '给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。'

"""
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
"""


class Solution:
    def convertToTitle(self, num: int) -> str:
        # 这道题的本质应该是将 十进制的数转换成26进制的表示
        res = ""
        while num > 0:
            num -= 1
            res += chr(num % 26 + ord('A'))
            num //= 26
        return res[::-1]


if __name__ == "__main__":
    num = 2147483647    # 答案为'FXSHRXW'
    print(Solution().convertToTitle(num))