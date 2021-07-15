__time__ = '2021/7/6'
__author__ = 'ZhiYong Sun'

"""给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        left = 0
        mx = 0

        for ind, ch in enumerate(s):
            if ch in hashmap:
                left = max(left, hashmap[ch] + 1)
            mx = max(mx, ind - left + 1)
            hashmap[ch] = ind

        return mx


if __name__ == "__main__":
    s = "abcabcbb"
    s = "bbbbb"
    result = Solution().lengthOfLongestSubstring(s)
    print(result)
