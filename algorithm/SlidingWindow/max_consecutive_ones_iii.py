"""
[最大连续1的个数 III](https://leetcode-cn.com/problems/max-consecutive-ones-iii/)
转换为最长子序列且序列中 0 的个数 <= K
"""


def longestOnes(A, K):
    N = len(A)
    res = 0
    left, right = 0, 0
    zeros = 0
    while right < N:
        if A[right] == 0:
            zeros += 1
        while zeros > K:
            if A[left] == 0:
                zeros -= 1
            left += 1
        res = max(res, right - left + 1)
        right += 1
    return res

