__time__ = '2021/8/14'
__author__ = 'ZhiYong Sun'


"""
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，

还有一个 random 指针指向链表中的任意节点或者 null。

"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited = {}
        def _dfs(node):
            if not node: return None
            if node in visited: return visited[node]
            root = Node(node.val)
            visited[node] = root
            root.next = _dfs(node.next)
            root.random = _dfs(node.random)
            return root
        return _dfs(head)

