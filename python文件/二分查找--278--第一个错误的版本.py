__time__ = '2021/7/15'
__author__ = 'ZhiYong Sun'


"""
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用bool isBadVersion(version)接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

求解 -- 以下直接用bad来替换了isBadVersion(version)接口
"""

"""该问题为标准二分查找的变体：
    ----条件为 left<right； 
    ----因此循环退出条件为left == right， 而非正常的判断退出
    ----mid始终落在区间的中间或者中间靠左，和 left = mid + 1 可以保证最后一定会有left==right
    ----从而避免死循环    
"""


class Solution:
    def firstBadVersion(self, n, bad):
        left, right = 1, n
        while left < right: # 循环退出条件为left==right
            mid = left + (right - left) // 2
            if mid < bad:
                left = mid + 1     # mid总是落在区间的中间或者靠左边，left=mid+1则保证了最后一定可以left==right
            else:
                right = mid
        return right


if __name__ == "__main__":
    n, bad = 5, 4
    print(Solution().firstBadVersion(n, bad))