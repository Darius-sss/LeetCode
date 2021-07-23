__time__ = '2021/7/20'
__author__ = 'ZhiYong Sun'
__doc__ = '请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。'


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def list_to_tree(arr):
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


def level_order(root):
    if not root: return []
    nums, stack = [], [root]
    while stack:
        nums.append([node.val for node in stack])
        tmp = []
        for node in stack:
            if node.left: tmp.append(node.left)
            if node.right: tmp.append(node.right)
        stack = tmp
    return nums


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(A, B):
            if not A and not B: return True
            if not A or not B or A.val != B.val: return False
            return dfs(A.right, B.left) and dfs(A.left, B.right)

        return dfs(root.left, root.right) if root else True


if __name__ == "__main__":
    root = list_to_tree([1, 2, 2, 3, 4, 4, 3])
    print(Solution().isSymmetric(root))

    arr = [1, 2, 2, 'null', 3, 'null', 3]
    print(Solution().isSymmetric(list_to_tree(arr)))
