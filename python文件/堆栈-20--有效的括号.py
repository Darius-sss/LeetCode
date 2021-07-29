__time__ = '2021/7/29'
__author__ = 'ZhiYong Sun'


"""

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
 
"""


class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', ']':'[', '}':'{'}
        stack = ['?']
        for ch in s:
            if ch not in hashmap:
                stack.append(ch)
            else:
                if hashmap[ch] != stack.pop():
                    return False
        return len(stack) == 1


if __name__ == "__main__":
    s = "()"
    print(Solution().isValid(s))

    s = "()[]{}"
    print(Solution().isValid(s))

    s = "(]"
    print(Solution().isValid(s))

    s = "([)]"
    print(Solution().isValid(s))

    s = "{[]}"
    print(Solution().isValid(s))