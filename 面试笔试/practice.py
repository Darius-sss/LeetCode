__time__ = '2021/8/7'
__author__ = 'ZhiYong Sun'

import collections

"""001--根据列表构造链表"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def _001(arr):
    head = None
    for num in arr[::-1]:
        head = ListNode(num, head)
    return head


"""002--根据链表转换成列表"""
def _002(head):
    if not head:
        return None
    nums = []
    while head:
        nums.append(head.val)
        head = head.next
    return nums


"""003--判断是否存在环形链表"""
def _003(head):
    if not head or not head.next :
        return False
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


"""004--判断环形链表的入环点"""
def _004(head):
    if not head or not head.next:
        return None
    slow, fast = head, head.next
    while slow != fast:
        if not (fast and fast.next):
            return None
        slow = slow.next
        fast = fast.next.next

    slow = slow.next  # 相遇之后slow再往前一步
    new = head   # 新指针从头开始

    while slow != new:
        slow, new = slow.next, new.next

    return slow


"""005--寻找链表的中间节点"""
def _005(head):
    if not head:
        return None
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


"""006--链表反转"""
def _006(head):
    if not head or not head.next:
        return head
    pre = None
    curr = head
    while curr:
        curr.next, pre, curr = pre, curr, curr.next
    return pre


"""007--链表交换邻接节点"""
def _007(head):
    if not (head and head.next):
        return head
    first, second = head, head.next
    first.next = _007(head.next.next)
    second.next = first
    return second


"""008--链表k个一组反转"""
def _008(head, k):
    curr = head

    for _ in range(k):
        if not curr:
            return head
        curr = curr.next

    pre, curr = None, head
    for _ in range(k):
        curr.next, pre, curr = pre, curr, curr.next

    head.next = _008(curr, k)

    return pre


"""009--两数之和"""
def _009(nums, target):
    hashmap = {}
    for ind, num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target-num], ind]
        hashmap[num] = ind
    return False


"""010--三数之和"""
def _010(nums):
    if len(nums) <= 3:
        return None
    nums.sort()
    res = []

    for ind, num in enumerate(nums):
        if num > 0:    # 优化
            break
        if ind >= 1 and num == nums[ind-1]: continue   # 避免重复
        left, right = ind + 1, len(nums) - 1

        while left < right:
            _sum = num + nums[left] + nums[right]
            if _sum == 0:
                res.append([num, nums[left], nums[right]])
                while left < right and nums[left+1] == nums[left]: left += 1
                while left < right and nums[right-1] == nums[right]: right -= 1
                left += 1
                right -= 1

            elif _sum < 0:
                left += 1
            else:
                right -= 1
    return res


"""011--无重复字符的最长子串"""
def _011(s):
    hashmap = collections.defaultdict(int)
    left = 0
    mx = 0

    for ind, ch in enumerate(s):
        left = max(left, hashmap[ch])
        mx = max(mx, ind - left)
        hashmap[ch] = ind
    return mx


"""012--变位词组"""
def _012(strs):
    hashmap = collections.defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))
        hashmap[key] += [word]

    return [item for item in hashmap.values()]


"""013--根据列表构建最低二叉树"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def _013(nums):
    if not nums: return None
    root = TreeNode(nums[0])
    stack = [root]
    front, index = 0, 1

    while index < len(nums):
        node = stack[front]
        front += 1

        node.left = TreeNode(nums[index])
        stack.append(node.left)

        index += 1
        if index >= len(nums): break
        node.right = TreeNode(nums[index])
        stack.append(node.right)
        index += 1
    return root


"""014--根据列表（leetcode形式)构建唯一二叉树"""
def _014(arr):
    if not arr: return None
    root = TreeNode(int(arr[0]))
    stack = [root]
    front = 0
    index = 1
    while index < len(arr):
        node = stack[front]
        front += 1

        item = arr[index]
        index += 1
        if item != "null":
            node.left = TreeNode(item)
            stack.append(node.left)

        if index >= len(arr):
            break

        item = arr[index]
        index += 1
        if item != "null":
            node.right = TreeNode(item)
            stack.append(node.right)
    return root


"""015--前序遍历-递归"""
def _015(root):
    if not root: return []
    return [root.val] + _015(root.left) + _015(root.right)


"""016--前序遍历-迭代"""
def _016(root):
    if not head: return []
    res, stack = [], []
    while stack or root:
        while root:
            res.append(root.val)
            stack.append(root)
            root = root.left
        root = stack.pop()
        root = root.right
    return res


"""017--中序遍历--递归"""
def _017(root):
    if not root: return []
    return _017(root.left) + [root.val] + _017(root.right)


"""018--中序遍历--迭代"""
def _018(root):
    if not root: return []
    res, stack = [], []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res


"""019--后序遍历-递归"""
def _019(root):
    if not root: return []
    return _019(root.left) + _019(root.right) + [root.val]


"""020--后序遍历-迭代"""
def _020(root):
    if not root: return []
    res, stack, prev = [], [], None
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if not root.right or root.right == prev:
            res.append(root.val)
            prev, root = root, None
        else:
            stack.append(root)
            root = root.right
    return res


"""021--层序遍历-迭代"""
def _021(root):
    if not root: return []
    res, stack = [], [root]
    while stack:
        res.append([node.val for node in stack])
        tmp = []
        for node in stack:
            if node.left: tmp.append(node.left)
            if node.right: tmp.append(node.right)
        stack = tmp
    return res


"""022--树的深度"""
def _022(root):
    if not root: return 0
    return max(_022(root.left), _022(root.right)) + 1


"""023--树的宽度"""
def _023(root):    # 本质就是对所有的节点求其左右深度
    length = 0
    def dfs(root):
        nonlocal length  # nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量
        if not root: return 0  # 访问到空节点了，返回0
        l = dfs(root.left)  # 左儿子为根的子树的深度
        r = dfs(root.right)  # 右儿子为根的子树的深度
        length = max(l + r, length)  # 当前节点的直径与直径比较
        return max(l, r) + 1  # 返回上层则时候子树根节点和其双亲节点之间还有一条边

    dfs(root)
    return length


"""024--由前序和中序构造二叉树"""
def _024(preorder, inorder):
    if not (preorder and inorder):
        return None

    # 根据前序数组的第一个元素，就可以确定根节点
    root = TreeNode(preorder[0])

    # 用preorder[0]去中序数组中查找对应的元素
    mid_idx = inorder.index(preorder[0])

    # 递归的处理前序数组的左边部分和中序数组的左边部分
    # 递归处理前序数组右边部分和中序数组右边部分
    root.left = _024(preorder[1:mid_idx + 1], inorder[:mid_idx])
    root.right = _024(preorder[mid_idx + 1:], inorder[mid_idx + 1:])

    return root


"""025--青蛙跳台阶问题"""
def _025(n):
    l, r = 1, 1
    for _ in range(n):
        l, r = r, l + r
    return l


"""026--购买股票问题-购买无限次"""
def _026(prices):
    buy, sell = -float('inf'), 0
    for p in prices:
        buy = max(buy, sell - p)
        sell = max(sell, buy + p)
    return sell


"""027--购买股票问题-购买一次"""
def _027(prices):
    buy, sell = -float('inf'), 0
    for p in prices:
        buy = max(buy, 0-p)
        sell = max(sell, buy + p)
    return sell


"""028--购买股票问题-购买两次"""
def _028(prices):
    buy1, buy2, sell1, sell2 = -float('inf'), -float('inf'), 0, 0
    for p in prices:
        buy1 = max(buy1, 0-p)
        sell1 = max(sell1, buy1 + p)
        buy2 = max(buy2, sell1 - p)
        sell2 = max(sell2, buy2 + p)
    return sell2


"""029--购买股票问题-购买k次"""
def _029(prices, k):
    buy = [-float('inf')] * (k + 1)
    sell = [0] * (k + 1)
    for p in prices:
        for k in range(1, k + 1):
            buy[k] = max(buy[k], sell[k-1] - p)
            sell[k] = max(sell[k], buy[k] + p)
    return sell[-1]


"""030--购买股票问题-购买无限次但有一天冷却时间"""
def _030(prices):
    buy, pre_sell, sell = -float('inf'), 0, 0
    for p in prices:
        buy = max(buy, pre_sell - p)
        pre_sell = sell
        sell = max(sell, buy + p)

    return sell


"""031--购买股票问题-购买无限次但有手续费"""
def _031(prices, fee):
    buy, sell = -float('inf'), 0
    for p in prices:
        buy = max(buy, sell - p - fee)
        sell = max(sell, buy + p)
    return sell


"""032--最大子序和"""
def _032(nums):
    n = len(nums)
    if n == 0: return '-inf'
    dp = [-float('inf')] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i-1] + nums[i-1], nums[i-1])
    return max(dp)


"""033--乘积最大子序列"""
def _033(nums):
    n = len(nums)
    if n == 0: return 0
    mx, mn, ans = nums[0], nums[0], nums[0]

    for i in range(1, n):
        mx, mn = max(mx * nums[i], mn * nums[i], nums[i]), min(mx * nums[i], mn * nums[i], nums[i])
        ans = max(mx, ans)
    return ans


"""039--快排"""
def _039(nums):
    if len(nums) < 2:
        return nums
    pivot = nums[0]
    less = [i for i in nums[1:] if i <= pivot]
    greater = [i for i in nums[1:] if i > pivot]
    return _039(less) + [pivot] + _039(greater)


# 原地快排
def partition(nums, p, r):
    x = nums[r]
    i = p - 1
    for j in range(p, r - 1):
        if nums[j] <= x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[r] = nums[r], nums[i + 1]
    return i + 1


def _039_2(nums, p, r):
    if p < r:
        q = partition(nums, p, r)
        _039_2(nums, p, q-1)
        _039_2(nums, q + 1, r)
    return nums


if __name__ == "__main__":
    # 001
    arr = [1, 2, 3, 4, 5]
    head = _001(arr)
    print(head)

    # 002
    nums = _002(head)
    print(nums)

    # 006
    print(_002(_006(head)))

    # 007
    head = _001([1, 2, 3, 4, 5])
    print(_002(_007(head)))

    # 008
    head = _001([1, 2, 3, 4, 5, 6, 7])
    print(_002(_008(head, 3)))

    # 009
    nums = [1, 2, 3, 4, 5, 7]
    print(_009(nums, 8))

    # 010
    nums = [-1, 0, 1, 2, -1, -4]
    print(_010(nums))

    # 011
    s = "abcabcbb"
    print(_011(s))

    # 012
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(_012(strs))

    # 013
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    root1 = _013(nums)

    # 014
    root2 = _014(nums)

    # 015
    print(_015(root1))

    # 016
    print(_016(root2))

    # 017
    print(_017(root1))

    # 018
    print(_018(root2))

    # 019
    print(_019(root2))

    # 020
    print(_020(root2))

    # 021
    print(_021(root2))

    # 022
    print(_022(root2))

    # 026
    prices = [7, 2, 6, 1, 6, 4, 8, 9, 18, 3, 5, 7, 4, 7]
    print(_026(prices))

    # 027
    print(_027(prices))

    # 028
    print(_028(prices))

    # 029
    prices = [7, 2, 6, 1, 6, 4, 8, 9, 18, 3, 5, 7, 4, 7]
    print(_029(prices, 4))

    # 030
    print(_030(prices))

    # 031
    print(_031(prices, 1))

    # 032
    nums = [-7, 2, -6, 1, 6]
    print(_032(nums))

    # 033
    nums = [-4, -3, -2]
    print(_033(nums))

    # 39
    nums = [7, 2, 6, 1, 6, 4, 8, 9, 18, 3, 5, 7, 4, 7]
    print(_039(nums))