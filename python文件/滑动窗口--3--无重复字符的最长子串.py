__time__ = '2021/7/20'
__author__ = 'ZhiYong Sun'
__doc__ = '给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。'

import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word = collections.defaultdict(int)
        count = 0
        left = 0                       # left 窗口左侧
        for right, ch in enumerate(s):  # right 窗口右侧

            if ch in word:
                left = max(left, word[ch] + 1)    # 如果字符曾经出现过，则更新left（只有当重复字符比left大时才会更新）

            count = max(count, right - left + 1)   # 更新count
            word[ch] = right   # 更新word
        return count


if __name__ == "__main__":
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))