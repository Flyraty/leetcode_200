"""
[数组的度](https://leetcode-cn.com/problems/degree-of-an-array)
"""
import collections


def findShortestSubArray(nums):
    # 找到所有元素的索引
    n = len(nums)
    d = collections.defaultdict(list)
    for i in range(n):
        d[nums[i]].append(i)
    # 按照出现次数排序
    tmp = sorted(d, key=lambda x: len(d[x]), reverse=True)
    # 确定数组的度
    degree = len(d[tmp[0]])
    res = 50000
    # 遍历，因为可能有多个符合数组的度的条件，需要找最短的
    for index in tmp:
        if len(d[index]) == degree:
            res = min(res, d[index][-1] - d[index][0] + 1)
        else:
            break
    return res
