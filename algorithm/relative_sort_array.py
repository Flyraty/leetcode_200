"""
[数组的相对排序](https://leetcode-cn.com/problems/relative-sort-array/)
"""


class Solution:
    def relativeSortArray(self, arr1, arr2):
        # 找到指定元素的所有下标
        def find_indexs(arr1, num):
            return [x[0] for x in enumerate(arr1) if x[1] == num]

        # 结果集
        res = []
        # 差集，在 arr1 不在 arr2
        no_arr2 = []
        for i in arr1:
            if i not in arr2:
                no_arr2.append(i)
        # 排序
        no_arr2.sort()
        # 交集按照 arr2 进行排序
        for j in arr2:
            if j not in no_arr2:
                res.extend([arr1[i] for i in find_indexs(arr1, j)])
        # 合并数据集
        res.extend(no_arr2)
        return res
