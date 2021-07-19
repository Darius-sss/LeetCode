__time__ = '2021/7/19'
__author__ = 'ZhiYong Sun'


class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')


if __name__ == "__main__":
    s = 'we are happy.'
    print(Solution().replaceSpace(s))
