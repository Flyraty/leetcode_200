"""
搜索,排序
1. 二分查找
2. 冒泡排序
3. 选择排序
4. 快速排序
5. 归并排序
6. 插入排序
"""


def binary_search(sort_seq, val):
    """
    是对已经排好序的数组查找
    :param sort_seq:
    :param val:
    :return:
    """
    low = 0
    high = len(sort_seq) - 1
    while low <= high:
        mid = (high + low) // 2
        if sort_seq[mid] == val:
            return mid
        elif val < sort_seq[mid]:
            high = mid - 1
        else:
            low = high + 1
    return low


def bubble_sort(seq):
    """
    冒泡排序
    :param seq:
    :return:
    """
    n = len(seq)
    for i in range(n):
        for j in range(n - 1 - i):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
    return seq


def select_sort(seq):
    """
    选择排序, 类似于打扑克牌, 发完全部牌后, 在每次找小的进行交换排序. 假定第一个最小, 拿最小的和剩余的比较，如果还有更小的那么则交换。如果没有, 接着下一轮
    :return:
    """
    n = len(seq)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if seq[j] < seq[i]:
                min = j
        if min != i:
            seq[i], seq[min] = seq[min], seq[i]
    return seq


def insert_sort(seq):
    """
    插入排序，类似于打扑克牌, 发一张牌，就和前面的比较一下, 牌发完后，排序也完成了, 假定第一个元素就是一个排序好的列表, 依次从后向前搜索, [1, 2] -> [1], [2] -> 2 > 1, no swap, 这就是排序好的数组
    :return:
    """
    n = len(seq)
    for i in range(1, n):
        value = seq[i]
        pos = i
        while pos > 0 and value < seq[pos - 1]:
            seq[pos] = seq[pos - 1]
            pos -= 1
        seq[pos] = value
    return seq


def partition(seq):
    """
    找到一个分组标准, 而不是使用默认第一个seq[0]
    cycle process:


    :param seq: [5, 9, 1, 11, 6, 7, 2, 4] ->
    :return:
    """
    left = 0
    right = len(seq) - 1
    pivotkey = seq[left]

    while left < right:
        while left < right and seq[right] >= pivotkey:
            right -= 1
        seq[left] = seq[right]
        while left < right and seq[left] <= pivotkey:
            left += 1
        seq[right] = seq[left]

    seq[left] = pivotkey
    return left


def quick_sort(seq):
    """
    快速排序, 分治策略, 复杂问题拆分成多个类似子问题, 递归解决
    :param seq:
    :return:
    """
    if len(seq) < 2:
        return seq
    value = seq[0]
    less_than_seq = [x for x in seq if x < value]
    more_than_seq = [x for x in seq if x > value]
    return quick_sort(less_than_seq) + value + quick_sort(more_than_seq)


def merge(list1, list2):
    """
    归并排序
    :param seq:  [3, 1], [2, 4, 0]
    :return:
    """
    new_list = list()
    a = b = 0
    while a < len(list1) and b < len(list2):
        if list1[a] < list2[b]:
            new_list.append(list1[a])
            a += 1
        else:
            new_list.append(list2[b])
            b += 1

    while a < len(list1):
        new_list.append(list1[a])
        a += 1

    while b < len(list2):
        new_list.append(list2[b])
        b += 1

    return new_list


def merge_sort(seq):
    """归并排序"""
    if len(seq) <= 1:
        return seq
    mid = int(len(seq) / 2)
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge(left, right)


if __name__ == '__main__':
    l = [5, 9, 1, 11, 6, 7, 2, 4]
    l2 = [1, 2]
    partition(l)
    print(merge_sort(merge(l, l2)))
