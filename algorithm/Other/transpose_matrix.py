"""
[转置矩阵](https://leetcode-cn.com/problems/transpose-matrix/)
"""


def transpose(matrix):
    res = list()
    for i in range(len(matrix[0])):
        res.append([x[i] for x in matrix])
    return res
