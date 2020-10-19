"""
[查找常用字符](https://leetcode-cn.com/problems/find-common-characters/)
"""


def commonChars(A):
    res = []
    if not A: return res
    for k in set(A[0]):
        num = min([a.count(k) for a in A])
        res += [k] * num
    return res
