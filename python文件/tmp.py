from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        candidate_k = [nums[n - 1]]
        max_k = float("-inf")

        for i in range(n - 2, -1, -1):
            if nums[i] < max_k:
                return True
            while candidate_k and nums[i] > candidate_k[-1]:   # 使得max_k小于nums[i]并且尽可能大
                max_k = candidate_k[-1]
                candidate_k.pop()
            if nums[i] > max_k:      # 如果nums[i]比max_k还要大，那么将其添加到单调栈中
                candidate_k.append(nums[i])

        return False


if __name__ == '__main__':
    nums = [3, 1, 4, 2]
    print(Solution().find132pattern(nums))