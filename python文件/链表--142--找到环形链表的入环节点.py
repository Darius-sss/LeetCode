__time__ = '2021/7/12'
__author__ = 'ZhiYong Sun'
"""
返回环形链表的入环节点
(a+b)*2 = a-1+b + (b+c)*n  --> a = c-1 + (b+c)*(n-1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def createCycle(self, nums, k):
        assert k < len(nums), 'k值设置大于链表长度'
        head = node = ListNode()
        count = 0
        for num in nums:
            node.next = ListNode(num)
            node = node.next
            count += 1
            if count == k:
                temp = node
        node.next = temp
        return head.next


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        slow, fast = head, head.next
        flag = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break
        if not flag:   # 如果无环  返回NULL
            return None
        new = head
        slow = slow.next
        while new != slow:
            new = new.next
            slow = slow.next
        print(slow.val)
        return slow


if __name__ == "__main__":
    nums = [1, 2, 0, 4, 6, 7]
    root = ListNode().createCycle(nums, 3)
    result = Solution().detectCycle(root)