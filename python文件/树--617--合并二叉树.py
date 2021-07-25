__time__ = '2021/7/23'
__author__ = 'ZhiYong Sun'

"""
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为NULL 的节点将直接作为新二叉树的节点。

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):    # 定义树
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(arr):    # 构造树
    if not arr: return None
    root = TreeNode(arr[0])
    stack = [root]
    front = 0
    index = 1
    while index < len(arr):
        node = stack[front]
        front += 1

        num = arr[index]
        index += 1
        if num != 'null':
            node.left = TreeNode(num)
            stack.append(node.left)

        if index >= len(arr): break

        num = arr[index]
        index += 1
        if num != 'null':
            node.right = TreeNode(num)
            stack.append(node.right)
    return root


def level_order(root):   # 层序遍历
    if not root: return []
    nums = []
    stack = [root]
    while stack:
        nums.append([node.val for node in stack])
        tmp = []
        for node in stack:
            if node.left: tmp.append(node.left)
            if node.right: tmp.append(node.right)
        stack = tmp
    return nums


class Solution:    # main
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:

        if not root1: return root2
        if not root2: return root1

        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTrees(root1.right, root2.right)
        return merged


if __name__ == "__main__":
    root1 = list_to_tree([1, 3, 2, 5])
    root2 = list_to_tree([2, 1, 3, 'null', 4, 'null', 7])
    res = Solution().mergeTrees(root1, root2)
    print(level_order(res))


