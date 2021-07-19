__time__ = '2021/7/19'
__author__ = 'ZhiYong Sun'
__doc__ = '根据前序遍历和中序遍历确定一棵树'

from typing import List


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def pre_order(root):
    if not root: return []
    return [root.val] + pre_order(root.left) + pre_order(root.right)


def in_order(root):
    if not root: return []
    return in_order(root.left) + [root.val] + in_order(root.right)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:inorder.index(preorder[0])+1], inorder[:inorder.index(preorder[0])])
        root.right = self.buildTree(preorder[inorder.index(preorder[0])+1:], inorder[inorder.index(preorder[0])+1:])
        return root


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    res = Solution().buildTree(preorder, inorder)
    print(pre_order(res))
    print(in_order(res))


