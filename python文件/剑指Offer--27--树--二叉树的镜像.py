__time__ = '2021/7/20'
__author__ = 'ZhiYong Sun'
__doc__ = '请完成一个函数，输入一个二叉树，该函数输出它的镜像。'


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


def level_order(root):   # 这里其实不应该使用层序遍历来看结果是否正确，应该使用tree_to_node（这部分代码还没写过）
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
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        head = TreeNode(root.val)
        head.left = self.mirrorTree(root.right)
        head.right = self.mirrorTree(root.left)
        return head


if __name__ == "__main__":
    root = list_to_tree([1, 2, 2, 3, 4, 4, 3])
    print(level_order(root))

    # [4, 2, 7, 1, 3, 6, 9]  --> [4, 7, 2, 9, 6, 3, 1]
    root = list_to_tree([4, 2, 7, 1, 3, 6, 9])
    res = Solution().mirrorTree(root)
    print(level_order(res))