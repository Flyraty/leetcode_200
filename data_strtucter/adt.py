"""
ADT抽象数据类型 -> 指一个数学模型以及定义在此数学模型上的一组操作。
1. 像基本数据类型int, str一样, 不用去关心内部实现, 可以直接拿来使用。
2. 抽象数据类型可以看作是描述问题的模型，它独立于具体实现。它的优点是将数据和操作封装在一起，使得用户程序只能通过在ADT里定义的某些操作来访问其中的数据，从而实现了信息隐藏。
"""


class Bag:
    """
    构造函数
    """
    def __init__(self):
        self._items = list()

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return _BagIterator(self._items)

    def __contains__(self, item):
        return item in self._items

    def add(self, item):
        self._items.append(item)

    def remove(self, item):
        assert item in self._items, 'item must be in the bag'


class _BagIterator:
    """
    实现了迭代器类
    """
    def __init__(self, seq):
        self._bag_items = seq
        self._cur_time = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_time < len(self._bag_items):
            item = self._bag_items[self._cur_time]
            self._cur_time += 1
            return item
        else:
            raise StopIteration


if __name__ == "__main__":
    bag = Bag()
    bag.add(1)
    bag.add(2)
    for i in bag:  # 隐藏了迭代器的实现
        print(i)

    i = bag.__iter__()
    while True:
        try:
            item = i.__next__()
            print(item)
        except StopIteration:
            break



