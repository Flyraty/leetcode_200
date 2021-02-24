"""
[水平翻转图片](https://leetcode-cn.com/problems/flipping-an-image/)
"""


def flipAndInvertImage(A):
    return [list(map(lambda x: 1 - x, row[::-1])) for row in A]
