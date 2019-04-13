"""
队列的实现, 只允许前端删除，后端插入
dequeue <-------------- enqueue

"""
from collections import namedtuple
from array_list import Array


class ListQueue:
    """
    列表实现queue, list存在复杂度退化
    1. list.append, 如果预先没有分配够内存, 那么会重新开辟空间, 复制之前的数据, 复杂度退化
    2. list.pop, pop不同位置会出现不同的复杂度, pop(-1)复杂度O(1), pop(0)复杂度O(n)
    """

    def __init__(self):
        self.qList = list()

    def is_empty(self):
        return len(self.qList) == 0

    def __len__(self):
        return len(self)

    def dequeue(self, value):
        self.qList.append(value)

    def enqueue(self):
        assert not self.is_empty()
        return self.qList.pop(0)


class ArrayQueue:
    """
    闭环数组实现queue,
    """

    def __init__(self, maxsize):
        self._front = 0
        self._back = maxsize - 1
        self._count = 0
        self.qArray = Array(maxsize)

    def is_empty(self):
        return self.qArray._size == 0

    def is_full(self):
        return self._count == len(self.qArray)

    def __len__(self):
        return self._count

    def enqueue(self, value):
        assert not self.is_full()
        maxSize = len(self.qArray)
        self._back = (self._back + 1) % maxSize
        self.qArray[self._back] = value
        self._count += 1

    def dequeue(self):
        assert not self.is_empty()
        item = self.qArray[self._front]
        maxSize = len(self.qArray)
        self._front = (self._front + 1) % maxSize
        self._count -= 1
        return item


class _QueueNode:
    def __init__(self, value):
        self.value = value


class LinkQueue:
    """
    链表实现queue
    """
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._qsize = 0
        self._count = 0

    def is_empty(self):
        return self._qhead is None

    def __len__(self):
        return self._count

    def enqueue(self, value):
        node = _QueueNode(value)
        if self.is_empty():
            self._qhead = node
        else:
            self._qtail.next = node
        self._qtail = node
        self._count += 1

    def dequeue(self):
        """
        删除头结点, 原先头结点的下一个结点成为新的头结点
        :return:
        """
        assert not self.is_empty(), "can't dequeue from a empty queue"
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None
            return node.value
        else:
            self._qhead = self._qhead.next
            self._count -= 1
            return node.value


class PriorityQueue:
    """
    无界优先队列
    1.优先级队列, 优先级高先出队列, 优先级相同FIFO方式出队列.
    2.list实现,时间复杂度O(n)
    """
    _PriorityQueue = namedtuple('PriorityQueue', 'value priority')

    def __init__(self):
        self._qlist = list()

    def __len__(self):
        return len(self._qlist)

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, value, priority):
        item = PriorityQueue._PriorityQueue(value, priority)
        self._qlist.append(item)

    def dequeue(self):
        """
        遍历元素, 找到最高优先级
        :return:
        """
        assert not self.is_empty()
        high = self._qlist[0]
        count = 0
        for i in range(0, len(self)):
            if self._qlist[i].priority > high.priority:
                high = self._qlist[i]
                count = i
        return self._qlist[count].value


class BoundedPriorityQueue:
    """
    有界优先队列, 要求优先级在一定范围内
    1. 一个优先级数组
    2. 每一个优先级对应着一个普通的优先级队列
    """

    def __init__(self, numLevels):
        self._qSize = 0
        self._qLevels = Array(numLevels)
        for i in range(numLevels):
            self._qLevels[i] = LinkQueue()

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        for i in range(len(self._qLevels)):
            self._qSize += len(self._qLevels[i])
        return self._qSize

    def enqueue(self, item, priority):
        """
        找到对应优先级维护的队列
        :param item:
        :param priority:
        :return:
        """
        assert 0 <= priority < len(self._qLevels), "Invalid priority level."
        self._qLevels[priority].enqueue(item)

    def dequeue(self):
        """
        找到第一个非空优先级队列
        :return:
        """
        assert not self.is_empty(), "Cannot dequeue from an empty queue."
        i = 0
        p = len(self._qLevels)
        while i < p:
            count = i
            if not self._qLevels[i].is_empty():
                break
            i += 1

        return self._qLevels[count].dequeue()


if __name__ == '__main__':
    lqueue = LinkQueue()
    lqueue.enqueue(1)
    lqueue.enqueue(2)
    print(lqueue.dequeue())

    bqueue = BoundedPriorityQueue(5)
    bqueue.enqueue('http', 3)
    bqueue.enqueue('https', 1)
    print(bqueue.dequeue())
