__time__ = '2021/7/19'
__author__ = 'ZhiYong Sun'
__doc__ = '输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。'

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_node(nums):
    head = None
    for num in nums[::-1]:
        head = ListNode(num, head)
    return head


def node_to_list(root):
    nums = []
    while root:
        nums.append(root.val)
        root = root.next
    return nums


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return nums[::-1]


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    res = Solution().reversePrint(list_to_node(nums))
    print(res)

