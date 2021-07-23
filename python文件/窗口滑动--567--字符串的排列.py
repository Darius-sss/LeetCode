__time__ = '2021/7/20'
__author__ = 'ZhiYong Sun'
__doc__ = '给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。' \
          '换句话说，第一个字符串的排列之一是第二个字符串的 子串 。' \
          '滑动窗口'


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        num1, num2 = [0] * 26, [0] * 26      # 使用数组来记录 字母a-z的个数
        for i in range(m):
            num1[ord(s1[i]) - ord('a')] += 1
            num2[ord(s2[i]) - ord('a')] += 1
        if num1 == num2:
            return True

        for j in range(m, n):
            num2[ord(s2[j - m]) - ord('a')] -= 1
            num2[ord(s2[j]) - ord('a')] += 1
            if num1 == num2:
                return True
        return False


if __name__ == "__main__":
    s1 = "adc"
    s2 = "dcda"
    print(Solution().checkInclusion(s1, s2))

    s1 = "ab"
    s2 = "eidbaooo"
    print(Solution().checkInclusion(s1, s2))