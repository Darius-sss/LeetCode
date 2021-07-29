__time__ = '2021/7/29'
__author__ = 'ZhiYong Sun'

from typing import List

"""
在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。

如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；

而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。

给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。

"""


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        num = label  # 确定二叉树有多少层, 可以使用库函数math.log2
        res = []
        while num:   # 每一行都是正向的结果，接下来需要做的是将偶数索引位置给换掉
            res.append(num)
            num >>= 1
        n = len(res)  # 二叉树层数

        for i in range(n):    # 对偶数层的位置进行替换
            if i & 1:
                res[i] = pow(2,n-i) - 1 - (res[i] - pow(2,n-i-1))     # 核心！！！

        return res[::-1]


if __name__ == "__main__":
    nums = [14, 26]
    for n in nums:
        print(Solution().pathInZigZagTree(n))
