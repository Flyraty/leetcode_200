"""
set: list实现
map: hash实现
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






