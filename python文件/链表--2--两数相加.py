__time__ = '2021/7/6'
__author__ = 'ZhiYong Sun'

"""
给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0开头。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):   # 定义链表结构
        self.val = val
        self.next = next

    def list_to_linkednode(self, nums):     # 建立链表
        head = None
        for num in nums[::-1]:
            head = ListNode(num, head)
        return head

    def linkednode_to_list(self, root):   # 将链表转成列表
        nums = []
        while root:
            nums.append(root.val)
            root = root.next
        return nums


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        carry = 0
        head = node = ListNode(0)

        while l1 or l2:
            if l1 and l2:
                carry, nextVal = divmod(l1.val + l2.val + carry, 10)
                l1 = l1.next
                l2 = l2.next
            elif l1:
                carry, nextVal = divmod(l1.val + carry, 10)
                l1 = l1.next
            else:
                carry, nextVal = divmod(l2.val + carry, 10)
                l2 = l2.next

            nextNode = ListNode(nextVal)
            node.next = nextNode
            node = node.next

        if carry:
            nextNode = ListNode(1)
            node.next = nextNode

        return head.next


if __name__ == "__main__":
    l1 = [2, 4, 6]
    l2 = [5, 6, 4]
    print(l1)
    print(l2)
    l1 = ListNode().list_to_linkednode(l1)
    l2 = ListNode().list_to_linkednode(l2)
    root = Solution().addTwoNumbers(l1, l2)
    result = ListNode().linkednode_to_list(root)
    print(ListNode().linkednode_to_list(l1))
    print(result)

