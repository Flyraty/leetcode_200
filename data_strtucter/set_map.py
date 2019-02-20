"""
set: list实现
map: 列表实现
时间复杂度排序: 1 < log(n) < n < nlog(n) < n^2 < n^3 < a^n
"""


class Set:
    """
    集合
    Set
    length
    contains
    add
    remove
    equals
    isSubsetOf
    union
    intersect
    difference
    iterator
    """

    def __init__(self):
        self._theElements = list()

    @property
    def __len__(self):
        return len(self._theElements)

    def __contains__(self, element):
        return element in self._theElements

    def add(self, element):
        if element not in self._theElements:
            self._theElements.append(element)

    def remove(self, element):
        assert element in self, 'element must be in set'
        self._theElements.remove(element)

    def __eq__(self, setB):
        if len(setB) != len(self._theElements):
            return False
        else:
            return self.isSubsetOf(setB)

    def isSubsetOf(self, setB):
        for element in setB:
            if element not in self:
                return False
        return True

    def union(self, setB):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self:
                newSet._theElements.append(element)
        return newSet


class Map:
    """
    Map() 字典
    add 添加map, 如果存在则修改
    valueOf 查询指定key的值
    remove 移除key
    findPosition 查询key的位置
    """

    def __init__(self):
        self._entryList = list()

    def __len__(self):
        return len(self._entryList)

    def __contains__(self, key):
        ndx = self._findPosition(key)
        return ndx is not None

    def add(self, key, value):
        ndx = self._findPosition(key)
        if ndx is not None:
            self._entryList[ndx].value = value
            return False
        else:
            entry = _MapEntry(key, value)
            self._entryList.append(entry)

    def valueOf(self, key):
        ndx = self._findPosition(key)
        assert ndx is not None, "Invaild map key"
        return self._entryList[ndx].value

    def remove(self, key):
        ndx = self._findPosition(key)
        assert key is not None, "Invaild map key"
        self._entryList.pop(ndx)

    def __iter__(self):
        return _MapIterator(self._entryList)

    def _findPosition(self, key):
        for i in range(len(self)):
            if self._entryList[i].key == key:
                return i
        return None


class _MapEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class _MapIterator:
    """

    """
    def __init__(self, entrylist):
        self._entryList = entrylist
        self._cur_time = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_time < len(self._entryList):
            key, value = self._entryList[self._cur_time].key, self._entryList[self._cur_time].value
            self._cur_time += 1
            return key, value
        else:
            raise StopIteration


if __name__ == '__main__':
    a = Map()
    a.add(1, 2)
    a.add(3, 4)
    a.add(5, 6)
    print(a.valueOf(1))
    for k, v in a:
        print('{}:{}'.format(k, v))

    a.add(1, 1)
    print(a.valueOf(1))
