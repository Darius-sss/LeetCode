__time__ = '2021/7/12'
__author__ = 'ZhiYong Sun'
__doc__ = 'K个一组反转链表'


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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = head
        for _ in range(k):    # 这一步仅仅只是用来判断链表剩余节点大于等于K
            if not curr:
                return head
            curr = curr.next

        pre, curr = None, head
        for _ in range(k):
            curr.next, pre, curr = pre, curr, curr.next

        head.next = self.reverseKGroup(curr, k)    # head原先是传进来的第一位，反转之后是传进来的最后一位，所以用head.next

        return pre


if __name__ == "__main__":
    nums = [num for num in range(1, 11)]
    root = ListNode().create_linked_node(nums)
    result = Solution().reverseKGroup(root, 3)
    print(ListNode().linked_node_to_list(result))
