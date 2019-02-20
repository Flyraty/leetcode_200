"""
链表结构
"""


class SingleNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prior = None


class SingleLink:
    """
    单链表
    """

    def __init__(self, node):
        self._head = node

    def __len__(self):
        cur = self._head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        return length

    def is_empty(self):
        return self._head == None

    def add(self, value):
        """
        头插
        :param node:
        :return:
        """
        node = SingleNode(value)
        node.next = self._head
        self._head = node

    def append(self, value):
        """
        尾插
        :param node:
        :return:
        """
        node = SingleNode(value)
        cur = self._head
        if self.is_empty():
            self._head = node
        else:
            while cur:
                cur = cur.next
            cur.next = node

    def remove(self, value):
        """
        先找到value, 每次遍历保存当前结点和前一个结点, 当找到删除结点时, 将前一个结点的指针指向当前结点的下一个结点
        :param value:
        :return:
        """
        cur = self._head
        prior = None
        while cur:
            if cur.value == value:
                if cur == self._head:
                    self._head = cur.next
                else:
                    prior.next = cur.next
                break
            else:
                prior = cur
                cur = cur.next

    def is_in_link(self, value):
        cur = self._head
        while cur:
            if cur.value == value:
                return True
            cur = cur.next
        return False

    def __iter__(self):
        cur = self._head
        while cur:
            print(cur.value)
            cur = cur.next


class DoubleLink:
    """
    双向链表
    """
    def __init__(self):
        self._head = SingleNode()
        self._tail = SingleNode()
        self._tail.next = self._head
        self._head.prior = self._tail

    def __len__(self):
        cur = self._head
        length = 0
        while cur.next == self._head:
            length += 1
            cur = cur.next
        return length

    def append(self, value):
        """
        在尾结点后面添加结点
        :param value:
        :return:
        """
        node = SingleNode(value)



