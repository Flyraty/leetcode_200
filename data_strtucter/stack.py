"""
栈结构, 后来居上, 后进先出
"""


class ListStack:
    """
    列表实现堆栈
    栈的peek和pop的区别, 都返回栈顶的值, 但是pop()在返回值的时候会同时删除栈顶
    """

    def __init__(self):
        self._entry = list()

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._entry)

    def pop(self):
        assert not self.is_empty()
        return self._entry.pop()

    def push(self, value):
        self._entry.append(value)

    def peek(self):
        return self._entry[-1]


class StackNode:
    def __init__(self, value, link):
        self.value = value
        self.next = link


class LinkStack:
    """
    链表实现堆栈
    """
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._top is None

    def pop(self):
        assert not self.is_empty()
        node = self._top
        self._top = self._top.next  # 栈顶等于原先栈顶的下一个结点
        self._size -= 1
        return node.value

    def push(self, value):
        self._top = StackNode(value, self._top)  # 栈顶元素
        self._size += 1

    def peek(self):
        assert not self.is_empty()
        return self._top.value


