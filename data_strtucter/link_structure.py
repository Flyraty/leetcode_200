"""
链表结构
"""


class SingleNode:
    def __init__(self, value):
        self.value = value
        self.next = None


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
        return self._head is None

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

    def travel(self):
        """
        到尾结点时已经跳出循环, 所以最后要打印一下尾结点
        :return:
        """
        cur = self._head
        while cur:
            print(cur.value)
            cur = cur.next
        print(cur.value)


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None


class DoubleCircleLink:
    """
    双向循环链表, 双向非循环列表和单链表的操作实现类似
    """

    def __init__(self, node):
        self._head = node

    def is_empty(self):
        return self._head is None

    def __len__(self):
        cur = self._head
        length = 0
        while cur.next != self._head:
            length += 1
            cur = cur.next
        return length

    def add(self, value):
        """
        头部插入元素
        :param value:
        :return:
        """
        node = DoubleNode(value)
        if self.is_empty():
            self._head = node
            node.next = node
            node.pre = node
        else:
            node.next = self._head
            node.pre = self._head.pre
            self._head.pre.next = node
            self._head.pre = node
            self._head = node

    def append(self, value):
        """
        尾插
        :param value:
        :return:
        """
        node = DoubleNode(value)
        if self.is_empty():
            self._head = node
            node.next = node
            node.pre = node
        else:
            node.next = self._head
            node.pre = self._head.pre
            self._head.pre.next = node
            self._head.pre = node

    def travel(self):
        if self.is_empty():
            return
        cur = self._head
        while cur.next != self._head:
            print(cur.value)
            cur = cur.next
        print(cur.value)

    def search(self, value):
        if self.is_empty():
            return
        cur = self._head
        while cur.next != self._head:
            if cur.value == value:
                return True
            cur = cur.next
        if cur.value == value:
            return True
        return False

    def insert(self, pos, value):
        """
        在pos位置插入Node(value), 遍历找到插入位置
        :param value:
        :return:
        """
        if pos == 0:
            self.add(value)
        elif pos > self.__len__() -1:
            self.add(value)
        else:
            index = 0
            cur = self._head
            while index < pos - 1:
                cur = cur.next
                index += 1
            node = DoubleNode(value)
            node.next = cur.next
            node.pre = cur
            cur.next.pre = node
            cur.next = node

    def remove(self, value):
        """
        先找到value
        :param value:
        :return:
        """
        if self.is_empty():
            return
        if not self.search(value):
            return
        cur = self._head
        while cur.next != self._head:
            if cur == self._head:
                if self.__len__() == 1:
                    self._head = None
                    return
                else:
                    self._head = cur.next
                    cur.next.pre = cur.pre
                    cur.pre.next = cur.next
                    return
            else:
                cur = cur.next
                if cur.value == value:
                    cur.next.pre = cur.pre
                    cur.pre.next = cur.next
                    return



