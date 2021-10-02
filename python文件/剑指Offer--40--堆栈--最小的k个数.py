__time__ = '2021/8/14'
__author__ = 'ZhiYong Sun'

import heapq
from typing import List

"""输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。"""

"""
解法：
1-排序（sort，或者实现快排(额外数组或者原地实现均可)）
2-堆
"""


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        return heapq.nsmallest(k, arr)


if __name__ == "__main__":
    arr = [3, 4, 5, 6, 1, 2, 7, 8]
    print(Solution().getLeastNumbers(arr, 4))