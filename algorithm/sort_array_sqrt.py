"""
[有序数组的平方](https://leetcode-cn.com/problems/squares-of-a-sorted-array/)
"""


def sort_array_sqrt(array):
    array.sort()
    return [x * x for x in array]
