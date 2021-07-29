__time__ = '2021/7/27'
__author__ = 'ZhiYong Sun'

"""
给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为2或0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。

更正式地说，root.val = min(root.left.val, root.right.val) 总成立。

给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def list_to_tree(arr):
    root = TreeNode(arr[0])
    stack = [root]
    front, index = 0, 1

    while index <= len(arr):
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


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root or not root.left:   # 题目中子节点是成对出现的，所以只要左节点没有则右节点也没有
            return -1
        left = root.left.val if root.left.val != root.val else self.findSecondMinimumValue(root.left)
        right = root.right.val if root.right.val != root.val else self.findSecondMinimumValue(root.right)

        return min(left, right) if min(left, right) != -1 else max(left, right)


# 或者使用先遍历转换成数组，再进行操作 O(nlogn) 要慢一些
class Solution_two:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def pre_order(root):
            if not root:
                return []
            return [root.val] + pre_order(root.left) + pre_order(root.right)
        nums = pre_order(root)
        new = sorted(list(set(nums)))
        return -1 if len(new) <= 1 else new[1]


if __name__ == "__main__":
    root = list_to_tree([1, 1, 3, 1, 1, 3, 4, 3, 1, 1, 1, 3, 8, 4, 8, 3, 3, 1, 6, 2, 1])
    print(Solution().findSecondMinimumValue(root))
    print(Solution_two().findSecondMinimumValue(root))

    root = list_to_tree([2, 2, 5, 'null', 'null', 5, 7])
    print(Solution().findSecondMinimumValue(root))
    print(Solution_two().findSecondMinimumValue(root))