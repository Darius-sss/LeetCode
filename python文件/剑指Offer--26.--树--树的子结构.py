__time__ = '2021/7/20'
__author__ = 'ZhiYong Sun'

"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。
"""


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def list_to_tree(arr):   # leetcode将初始arr构造成一棵树
    if not arr: return None
    root = TreeNode(arr[0])
    stack = [root]
    front = 0
    index = 1
    while index < len(arr):
        node = stack[front]         # 要添加左右子节点的根节点
        front += 1                  # 根节点+1

        num = arr[index]            # 添加左子节点，如果是 null 则说明为空
        index += 1
        if num != "null":
            node.left = TreeNode(num)
            stack.append(node.left)

        if index >= len(arr): break     # 如果index超过了长度，那就退出

        num = arr[index]          # 添加右子节点，如果为 null 则说明为空
        index += 1
        if num != "null":
            node.right = TreeNode(num)
            stack.append(node.right)
    return root


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def dfs(A, B):
            if not B: return True    # 如果B为空，则说明已经对比完毕
            if not A or A.val != B.val:   # 如果B不为空 但是A为空，或者两者的值不相等，则说明对比失败
                return False
            return dfs(A.left, B.left) and dfs(A.right, B.right)  # 如果当前对比成功，则继续往左右子节点进行对比

        return bool(A and B) and (dfs(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))


if __name__ == "__main__":
    A = list_to_tree([1, 2, 3])
    B = list_to_tree([3, 1])
    print(Solution().isSubStructure(A, B))

    A = list_to_tree([3, 4, 5, 1, 2])
    B = list_to_tree([4, 1])
    print(Solution().isSubStructure(A, B))