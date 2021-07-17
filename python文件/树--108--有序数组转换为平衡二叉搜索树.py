__time__ = '2021/7/17'
__author__ = 'ZhiYong Sun'
__doc__ = '高度平衡--满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」，其中，每个是关键！！！ ' \
          '二叉搜索树--满足左子树所有节点都小于根节点且右子树所有节点都大于根节点'


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def pre_order(self, root):
        if not root: return []
        return [root.val] + self.pre_order(root.left) + self.pre_order(root.right)

    def in_order(self, root):
        if not root: return []
        return self.in_order(root.left) + [root.val] + self.in_order(root.right)

    def post_order(self, root):
        if not root: return []
        return [root.val] + self.post_order(root.left) + self.post_order(root.right)


class Solution:  # 将一个严格递增的列表 转换成 一颗高度平衡的二叉搜索树
    def create(self, nums, left, right):
        if left > right:
            return None
        mid = left + (right - left) // 2
        root = TreeNode(nums[mid])
        root.left = self.create(nums, left, mid-1)
        root.right = self.create(nums, mid+1, right)
        return root


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    result = Solution().create(nums, 0, len(nums)-1)
    print(TreeNode().in_order(result))