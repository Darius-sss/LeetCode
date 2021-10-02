__time__ = '2021/8/22'
__author__ = 'ZhiYong Sun'

"""输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # 在中序遍历的框架之中，如果没有前节点标记为self.head，否则进行前节点后节点的指向
        def dfs(cur):
            if not cur: return
            dfs(cur.left)  # 递归左子树
            if self.pre:  # 修改节点引用
                self.pre.right, cur.left = cur, self.pre  # 前节点指向当前，当前节点指向前节点
            else:  # 记录头节点
                self.head = cur
            self.pre = cur  # 保存 cur
            dfs(cur.right)  # 递归右子树

        if not root: return
        self.pre = None  # 前节点初始为None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head  # 将头尾结点进行相连
        return self.head


# 测试见：
# https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/
