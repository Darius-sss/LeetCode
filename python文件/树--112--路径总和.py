__time__ = '2021/7/17'
__author__ = 'ZhiYong Sun'

"""
112--
给你二叉树的根节点root 和一个表示目标和的整数targetSum ，判断该树中是否存在 根节点到叶子节点的路径，
这条路径上所有节点值相加等于目标和targetSum 。
叶子节点 是指没有子节点的节点。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def stringToTreeNode(self, arr):   # leetcode将初始arr构造成一棵树
        if not arr: return None
        root = TreeNode(int(arr[0]))
        stack = [root]
        front = 0
        index = 1
        while index < len(arr):
            node = stack[front]
            front += 1

            item = arr[index]
            index += 1
            if item != "null":
                node.left = TreeNode(item)
                stack.append(node.left)

            if index >= len(arr):
                break

            item = arr[index]
            index += 1
            if item != "null":
                node.right = TreeNode(item)
                stack.append(node.right)
        return root

    def pre_order(self, root):
        if not root: return []
        return [root.val] + self.pre_order(root.left) + self.pre_order(root.right)


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if not (root.left or root.right):
            return root.val == targetSum
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)


if __name__ == "__main__":
    arr = [5, 4, 8, 11, 'null', 13, 4, 7, 2, 'null', 'null', 'null', 1]
    root = TreeNode().stringToTreeNode(arr)
    print(Solution().hasPathSum(root, 22))