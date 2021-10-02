class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



# class Solution:
#     def solve(self, m, a ):
#         # write code here
#         res = [ListNode(-1)] * m
#         cur = a
#         while cur:
#             tmp = cur.val
#             res[tmp % m].next = ListNode(tmp)
#             res[tmp % m] = res[tmp % m].next
#             print(tmp)
#             cur = cur.next
#         for i in range(m):
#             res[i] = res[i].next
#         ans = list(map(node_to_list, res))
#         return ans


class Solution:
    def solve(self, m, a ):
        def list_to_node(arr):
            cur = head = ListNode(-1)
            for num in arr:
                cur.next = ListNode(num)
                cur = cur.next
            return head.next

        def node_to_list(root):
            res = []
            while root:
                res.append(root.val)
                root = root.next
            return res

        res = []
        ans = []
        nums = node_to_list(a)
        for i in range(m):
            res.append([num for num in nums if num % m == i])
        for stack in res:
            if stack:
                ans.append(list_to_node(stack))
            else:
                ans.append(None)
        return ans

if __name__ == '__main__':
    arr = [7,8,13,11,15,0,10,15,9,9]
    m = 9
    root = list_to_node(arr)
    print(Solution().solve(9, root))



T = int(input())
for _ in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    res = 0
    for i in range(n):
        res += (nums[i] + nums[i] * (n - i) * (n - i - 1) / 2) % 1000000007
    print(int(res % 1000000007))




''' 8 2 1 4 1'''
'''1,1,1  == 1   2, 2    1+ 2 4'''

"""
2
5
8 2 1 4 1
2
1 2
"""

T = int(input())
for _ in range(T):
    n, w = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    weights.sort()
    count = 0
    while weights:
        n = weights[0]
        if n >= w:
            count += len(weights)
            break
        else:
            for j in range(len(weights)-1,0,-1):
                if weights[j] + n <= w and (weights[j] + n) % 2 == 0:
                    del weights[j]
                    break
            del weights[0]
            count += 1
    print(count)


# n, k = list(map(int, input().split()))
# word = input()
# res = ''
# words = list(word)
# cur = 0
# for _ in range(k):
#     _next = chr(ord('a')-1)
#     for i in range(cur, n-k+1):
#         if ord(words[i]) > ord(_next):
#             ind = i
#             _next = words[i]
#     cur = ind + 1
#     k -= 1
#     res += _next
#
# print(res)
#
# """
# 4 2
# ebfc
# """


"""9
4 5 2 2 1 3 5 5 11"""

1 + 1 + 2 + 1 + 6