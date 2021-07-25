import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = collections.OrderedDict()  # 有序字典，按添加顺序

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        value = self.dic.pop(key)
        self.dic[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                self.dic.popitem(last=False)  # last=False 先进先出  last=True 先进后出
        self.dic[key] = value