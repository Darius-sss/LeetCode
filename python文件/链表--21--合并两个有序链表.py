__time__ = '2021/7/24'
__author__ = 'ZhiYong Sun'
__doc__ = 'merge two sorted linked node'


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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = node = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        node.next = l1 if l1 else l2
        return res.next


if __name__ == "__main__":
    l1 = list_to_node([1, 2, 4])
    l2 = list_to_node([1, 3, 4])
    res = Solution().mergeTwoLists(l1, l2)
    print(node_to_list(res))
