__time__ = '2021/7/26'
__author__ = 'ZhiYong Sun'

"""
给你一个数组target，包含若干 互不相同的整数，以及另一个整数数组arr，arr可能 包含重复元素。

每一次操作中，你可以在 arr的任意位置插入任一整数。比方说，如果arr = [1,4,1,2]，那么你可以在中间添加 3得到[1,4,3,1,2]。你可以在数组最开始或最后面添加整数。

请你返回 最少操作次数，使得target成为arr的一个子序列。

一个数组的 子序列指的是删除原数组的某些元素（可能一个元素都不删除），同时不改变其余元素的相对顺序得到的数组。
比方说，[2,7,4]是[4,2,3,7,2,1,4]的子序列（加粗元素），但[2,4,2]不是子序列。

"""
from typing import List
import collections
import bisect


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # 解法二：转换为寻找严格递增子序列--使用二分法进行求解O(nlogn)
        hashmap = collections.defaultdict(int)  # 创建target中num和index的映射关系
        for i, num in enumerate(target):
            hashmap[num] = i

        new = [hashmap[num] for num in arr if num in hashmap]  # 该问题转换为寻找new的最长严格递增子序列长度

        # 使用二分查找确定最长严格递增公共子序列的长度
        n = len(new)
        total, q = 0, [0] * (n + 1)
        for i in range(n):
            index = bisect.bisect_left(a=q, x=new[i], lo=0, hi=total)
            if index == total:
                total += 1
            q[index] = new[i]

        return len(target) - total


if __name__ == "__main__":
    target = [6, 4, 8, 1, 3, 2]
    arr = [4, 7, 6, 2, 3, 8, 6, 1]
    print(Solution().minOperations(target, arr))