class listNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linkNode(root):
    head = listNode(0)
    res = head
    for i in range(len(root)):
        nextNode = listNode(root[i])
        head.next = nextNode
        head = head.next
    return res.next


if __name__ == '__main__':
    root = [1, 2, 3, 4, 5]
    res = linkNode(root)

    while res:
        print(res.val)
        res = res.next

