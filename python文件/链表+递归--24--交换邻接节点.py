__time__ = '2021/7/12'
__author__ = 'ZhiYong Sun'
__doc__ = '交换邻接节点'


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def list_to_linkednode(self, nums):     # 建立链表
        head = None
        for num in nums[::-1]:
            head = ListNode(num, head)
        return head

    def linkednode_to_list(self, root):
        nums = []
        while root:
            nums.append(root.val)
            root = root.next
        return nums


class Solution:   # 递归解法
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        first, second = head, head.next
        first.next = self.swapPairs(head.next.next)
        second.next = first

        return second


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    root = ListNode().list_to_linkednode(nums)
    print(ListNode().linkednode_to_list(root))
    result = Solution().swapPairs(root)
    print(ListNode().linkednode_to_list(result))