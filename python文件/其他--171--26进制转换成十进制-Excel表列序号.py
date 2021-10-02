__time__ = '2021/7/30'
__author__ = 'ZhiYong Sun'

""" 给定一个Excel表格中的列名称，返回其相应的列序号。 """


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        size = len(columnTitle)
        ans = 0

        for i in range(size - 1, -1, -1):
            ans += (ord(columnTitle[i]) - ord('A') + 1) * 26 ** (size - i - 1)

        return ans


if __name__ == "__main__":
    print(Solution().titleToNumber('AB'))
    print(Solution().titleToNumber('ZY'))
