__time__ = '2021/7/18'
__author__ = 'ZhiYong Sun'
__doc__ = '一个栈负责 add   一个栈负责delete ！'


class CQueue:

    def __init__(self):
        self.add = []   # add
        self.delete = []   # delete

    def appendTail(self, value: int) -> None:
        self.add.append(value)

    def deleteHead(self) -> int:
        if not (self.add or self.delete):   # 两个都为空则返回-1
            return -1
        elif not self.delete:       # delete为空但是add不为空，则将add中的添加到delete中
            while self.add:
                self.delete.append(self.add.pop())
            return self.delete.pop()

        return self.delete.pop()     # 如果delete本身就有，则返回最后一个

