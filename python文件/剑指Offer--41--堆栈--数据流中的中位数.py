__time__ = '2021/8/14'
__author__ = 'ZhiYong Sun'


"""
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

例如，
[2,3,4]的中位数是 3
[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：
void addNum(int num) - 从数据流中添加一个整数到数据结构中。
double findMedian() - 返回目前所有元素的中位数。
"""
import bisect

class MedianFinder_1:
    """第一种解法：使用二分查找维护一个有序数列"""

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.size = 0

    def addNum(self, num: int) -> None:
        index = bisect.bisect(self.nums, num)
        if index < self.size:
            self.nums.insert(index, num)
        else:
            self.nums.append(num)
        self.size += 1

    def findMedian(self) -> float:
        if self.size & 1:
            return self.nums[self.size//2]
        return (self.nums[self.size//2 - 1] + self.nums[self.size//2])/ 2


    
if __name__ == "__main__":
