"""
[N皇后 II](https://leetcode-cn.com/problems/n-queens-ii/)
n 皇后有几种解法
"""


def totalNQueens(n):
    col = set()
    pos = set()
    neg = set()
    res = 0

    def backtrack(i):
        nonlocal res
        if i == n:
            res += 1
            return
        for j in range(n):
            if j not in col and i - j not in pos and i + j not in neg:
                # 做选择
                col.add(j)
                pos.add(i - j)
                neg.add(i + j)
                # 递归进入下一行
                backtrack(i + 1)
                # 撤销选择
                col.remove(j)
                pos.remove(i - j)
                neg.remove(i + j)

    backtrack(0)
    return res
