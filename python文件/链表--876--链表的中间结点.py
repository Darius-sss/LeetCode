__time__ = '2021/7/19'
__author__ = 'ZhiYong Sun'
__doc__ = '寻找链表的中间节点'





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
    def middleNode(self, head: ListNode) -> ListNode:
        # 题目中给定的head不为空
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    root = list_to_node(nums)
    res = Solution().middleNode(root)
    print(node_to_list(res))

    nums1 = [1, 2, 3, 4, 5, 6, 7]
    root1 = list_to_node(nums1)
    res1 = Solution().middleNode(root1)
    print(node_to_list(res1))