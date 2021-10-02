__time__ = '2021/8/14'
__author__ = 'ZhiYong Sun'

"""定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.minstack:
            x = x if x < self.minstack[-1] else self.minstack[-1]
        self.minstack.append(x)

    def pop(self) -> None:
        if self.stack:
            del self.minstack[-1]
            del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
if __name__ == "__main__":
    """https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/"""