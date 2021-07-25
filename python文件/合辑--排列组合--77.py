__time__ = '2021/7/25'
__author__ = 'ZhiYong Sun'
__doc__ = 'itertools.permutations' \
          'itertools.combinations' \

"""
39--组合总和------从给定的列表（列表数字不重复）中选择数字（可重复选择）使其总和为target，输出所有选择！
40--组合总和II----从给定的列表（列表数字有重复）中选择数字（不可重复选择）使其总和为target，输出所有选择！
77--组合---------给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合，输出所有选择！
216--组合总和III--从[1-9]中找出所有相加之和为 n 的 k 个数的组合，输出所有选择！
377--组合总和Ⅳ---从给定的列表（列表数字不重复）中选择数字（可重复选择）使其总和为target，并且顺序不同则视为不同选择，输出选择的总数！

46--全排列
47--全排列II

78--子集
90--子集II
"""


from typing import List
from itertools import permutations
from itertools import combinations

"""
39--
给定一个无重复元素的正整数数组candidates和一个正整数target，找出candidates中所有可以使数字和为目标数target的唯一组合。

candidates中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。

对于给定的输入，保证和为target 的唯一组合数少于 150 个。

"""


class Solution_39:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def backtrack(tmp, _sum, cur):   # _sum表示当前的和, cur表示当前搜索的索引位置
            if _sum > target:            # 如果_sum超过target，结束该回溯
                return
            if _sum == target:           # 如果总和刚好为target，则将结果添加到res中，结束该回溯
                res.append(tmp)
                return
            for i in range(cur, n):      # 从当前以及之后的位置寻找一个加入
                backtrack(tmp + [candidates[i]], _sum + candidates[i], i)

        backtrack([], 0, 0)
        return res


"""
40--
给定一个数组candidates和一个目标数target，找出candidates中所有可以使数字和为target的组合。

candidates中的每个数字在每个组合中只能使用一次。

注意：解集不能包含重复的组合。

"""

class Solution_40:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()

        def backtrack(tmp, _sum, cur):   # _sum表示当前的和, cur表示当前搜索的索引位置
            if _sum > target:
                return
            if _sum == target:
                res.append(tmp)
                return
            for i in range(cur, n):
                # 每个位置上选择的数不能重复！比如[1,2,2,2,5]，选了第一个 2，变成 [1,2]，它的下一选项也是2，跳过它，因为如果选它就还是[1,2]
                if i > cur and candidates[i] == candidates[i-1]:
                    continue
                else:
                    backtrack(tmp + [candidates[i]], _sum + candidates[i], i + 1)   # 这里由i边成i+1,避免自身重复选择
        backtrack([], 0, 0)
        return res


"""
77--
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。
"""


class Solution_77:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(tmp, cur):   # cur表示当前搜索的索引位置
            if len(tmp) == k:
                res.append(tmp)
                return
            for i in range(cur, n + 1):
                backtrack(tmp + [i], i + 1)

        backtrack([], 1)
        return res


"""
216--
找出所有相加之和为n 的k个数的组合。组合中只允许含有 1 -9 的正整数，并且每种组合中不存在重复的数字。

说明：
所有数字都是正整数。
解集不能包含重复的组合。
"""


class Solution_216:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > 45:
            return []

        res = []

        def backtrack(tmp, _sum, cur):   # _sum表示sum(tmp), cur表示当前搜索到的位置
            if len(tmp) == k:  # 当tmp中有k个数字时
                if _sum == n:  # 如果刚好和为n，则添加到res中，否则不管是大还是小都返回False
                    res.append(tmp)
                return
            for i in range(cur, 10):  # 整体是从1就开始，到9结束
                backtrack(tmp + [i], _sum + i, i + 1)

        backtrack([], 0, 1)  # 从1开始
        return res


"""
377--
给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。

题目数据保证答案符合 32 位整数范围。

"""


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 思路是没有错，但是结果太多极其超时，不推荐使用该代码。
        res = []

        def backtrack(tmp, _sum):   # _sum表示sum(tmp)
            if _sum > target:       # 如果_sum超过target则结束回溯
                return
            if _sum == target:       # 如果_sum刚好是target则添加答案，结束该回溯
                res.append(tmp)
                return
            for i in range(len(nums)):   # 否则进行下一个点的选择
                backtrack(tmp + [nums[i]], _sum + nums[i])
        backtrack([], 0)
        return len(res)


class Solution_377:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 考虑到这道题目返回的结果只是个数，考虑动态规划
        dp = [1] + [0] * target   # 当n为0时，默认只有一种选法即什么都不选
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
        return dp[target]




class Solution_46:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # return list(map(list, itertools.permutations(nums)))  # 一行可解决
        res = []

        def dfs(nums, tmp):
            if not nums:
                res.append(tmp)
                return

            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:], tmp + [nums[i]])

        dfs(nums, [])
        return res


if __name__ == "__main__":
    # 39测试用例
    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution_39().combinationSum(candidates, target))

    # 40测试用例
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution_40().combinationSum2(candidates, target))

    # 77测试用例
    n, k = 8, 3
    print(Solution_77().combine(n, k))

    # 216测试用例
    k, n = 3, 9
    print(Solution_216().combinationSum3(k, n))

    # 377测试用例
    nums = [1, 2, 3]
    target = 4
    print(Solution_377().combinationSum4(nums, target))


    #
    # nums = [1, 2, 3]
    # print(Solution_46().permute(nums))