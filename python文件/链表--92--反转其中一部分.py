__time__ = '2021/7/12'
__author__ = 'ZhiYong Sun'

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create_linked_node(self, nums):
        head = None
        for num in nums[::-1]:
            head = ListNode(num, head)
        return head

    def linked_node_to_list(self, root):
        nums = []
        while root:
            nums.append(root.val)
            root = root.next
        return nums



class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(-1, head)
        pre, cur = dummy, head
        for _ in range(left-1):
            pre = pre.next
        cur = pre.next
        first, last = pre, cur   # 左侧断点的 前和后 两个节点

        for _ in range(right-left+1):  # 将中间部分进行倒序
            cur.next, pre, cur = pre, cur, cur.next

        first.next = pre
        last.next = cur
        return dummy.next


if __name__ == "__main__":
    nums = [num for num in range(10)]
    root = ListNode().create_linked_node(nums)
    result = Solution().reverseBetween(root, 4, 7)
    print(ListNode().linked_node_to_list(result))