__time__ = '2021/7/12'
__author__ = 'ZhiYong Sun'
__doc__ = '反转链表'


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
        _list = []
        while root:
            _list.append(root.val)
            root = root.next
        return _list


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, curr = None, head
        while curr:
            curr.next, pre, curr = pre, curr, curr.next
        return pre


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    root = ListNode().list_to_linkednode(nums)
    result = Solution().reverseList(root)
    print(ListNode().linkednode_to_list(result))
