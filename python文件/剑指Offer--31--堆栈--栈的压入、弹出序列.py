__time__ = '2021/8/22'
__author__ = 'ZhiYong Sun'

from typing import List

"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。

例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

"""


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # 如果栈的压入和弹出序列给出了，那么其中的操作是唯一确定的
        stack = []
        ind = 0
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[ind]:
                stack.pop()
                ind += 1
        return stack == []


if __name__ == "__main__":
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    print(Solution().validateStackSequences(pushed, popped))
