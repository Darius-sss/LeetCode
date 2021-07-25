__time__ = '2021/7/23'
__author__ = 'ZhiYong Sun'

"""
给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None

        stack = [root]

        while stack:
            for i in range(len(stack)-1):
                stack[i].next = stack[i+1]
            stack[-1].next = None

            tmp = []
            for node in stack:
                if node.left:        # 题意是完美二叉树，左边存在则右边存在
                    tmp.append(node.left)
                    tmp.append(node.right)
            stack = tmp

        return root




if __name__ == "__main__":
    "测试用例见LeetCode " \
    "https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/"