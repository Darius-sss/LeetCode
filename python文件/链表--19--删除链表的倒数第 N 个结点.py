__time__ = '2021/7/19'
__author__ = 'ZhiYong Sun'
__doc__ = '删除链表的倒数第N个节点' \
          '思路--先走n个节点，再一起走即可'


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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr = ListNode(0, head)    # 这里是要加一个伪头结点的，否则删除第一个节点时不好操作
        left, right = curr, curr.next

        for _ in range(n):
            right = right.next

        while right:          # 判断条件可以自己画个链表看一下
            left = left.next
            right = right.next
        left.next = left.next.next
        return curr.next


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    n = 5
    res = Solution().removeNthFromEnd(list_to_node(nums), n)
    print(node_to_list(res))

