"""
[O(1) 时间插入、删除和获取随机元素 - 允许重复](https://leetcode-cn.com/problems/insert-delete-getrandom-o1-duplicates-allowed/)
使用 list 维护元素列表，使用 dict 维护元素值索引。list append O(1) 时间复杂度插入，通过将要删除的元素与列表最后一个元素相交换 + pop 来达到 O(1) 删除元素
"""

import random


class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list1 = []
        self.dict1 = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        l_len = len(self.list1)
        v_set = self.dict1.get(val)
        self.list1.append(val)
        if v_set:
            self.dict1[val].add(l_len)
            return False
        else:
            self.dict1[val] = {l_len}
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        v_set = self.dict1.get(val)
        l_len = len(self.list1)
        if v_set:
            last_val = self.list1[-1]
            if val == last_val:
                v_set.remove(l_len - 1)
            else:
                v_index = v_set.pop()
                self.list1[v_index] = last_val
                last_set = self.dict1.get(last_val)
                last_set.remove(l_len - 1)
                last_set.add(v_index)
            self.list1.pop()
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.list1)
