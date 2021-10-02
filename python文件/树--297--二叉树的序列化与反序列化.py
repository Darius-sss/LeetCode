__time__ = '2021/8/22'
__author__ = 'ZhiYong Sun'


"""
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

"""

import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # 解法1 层序遍历方式
        if not root: return ''

        q = collections.deque([root])
        ans = []
        while q:
            node = q.popleft()
            ans.append(str(node.val) if node else 'null')
            if node: q.extend([node.left, node.right])
        return ','.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return

        nodes = [(TreeNode(int(v)) if v != 'null' else None) for v in data.split(',')]
        i, j = 0, 1
        while j < len(nodes):
            if nodes[i] is not None:
                nodes[i].left = nodes[j]
                j += 1
                nodes[i].right = nodes[j]
                j += 1
            i += 1
        return nodes[0]


def level_order(root):
    if not root: return []
    res, stack = [], [root]
    while stack:
        res.append([node.val for node in stack])
        tmp = []
        for node in stack:
            if node.left: tmp.append(node.left)
            if node.right: tmp.append(node.right)
        stack = tmp
    return res


if __name__ == '__main__':
    strs = "1,2,3,null,null,4,5,null,null,null,null"
    head = Codec().deserialize(strs)
    print(Codec().serialize(head))
    print(level_order(head))