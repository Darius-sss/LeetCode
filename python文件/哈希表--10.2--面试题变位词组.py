__time__ = '2021/7/18'
__author__ = 'ZhiYong Sun'
__doc__ = '编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。' \
          '解法--将排序后的word作为hashmap的key'


import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = collections.defaultdict(list)
        for word in strs:
            key = ' '.join(sorted(word))   # 注意一下这里，sorted返回的是列表
            hashmap[key] += [word]
        return [item for item in hashmap.values()]


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))