"""
[删除字符串中的所有相邻重复项](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/)
利用栈数据结构，和单调栈有点异曲同工之妙
"""


def removeDuplicates(S) -> str:
    stack = list()
    for s in S:
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
    return "".join(stack)
