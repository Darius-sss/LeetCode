__time__ = '2021/7/12'
__author__ = 'ZhiYong Sun'


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def createCycle(self, nums, k):
        assert k < len(nums)
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

    def list_to_linkednode(self, nums):
        head = None
        for num in nums[::-1]:
            head = ListNode(num, head)
        return head


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    nums = [1, 3, 4, 5, 7]
    root = ListNode().createCycle(nums, k=2)
    result = Solution().hasCycle(root)
    print(result)

    root2 = ListNode().list_to_linkednode(nums)
    result2 = Solution().hasCycle(root2)
    print(result2)
