from typing import List


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52   # 差分数组
        for l, r in ranges:
            diff[l] += 1
            diff[r+1] -= 1
        # 前缀和
        curr = 0
        for i in range(1, 51):
            curr += diff[i]           # 进行帕累托累加
            if left <= i <= right and curr <= 0:
                return False
        return True


if __name__ == '__main__':
    ranges = [[1, 2], [3, 4], [5, 6]]
    left = 2
    right = 5
    print(Solution().isCovered(ranges,left,right))

    nums= [1, 2, 3, 4, 5, 6]
    for i in range(1, len(nums)-1):
        nums[i] += nums[i-1]
    print(nums)