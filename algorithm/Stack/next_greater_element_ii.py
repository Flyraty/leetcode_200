"""
[下一个更大元素 II](https://leetcode-cn.com/problems/next-greater-element-i)
用单调栈 + 循环数组实现，单调递减栈
1. 开始循环遍历数组，元素入栈
2. 比较栈顶元素和当前元素的大小
    - 如果当前元素小于等于栈顶元素，继续将当前元素入栈
    - 如果当前元素大于栈顶元素， 栈中所有元素出栈，并记录这批元素的下一个最大值是当前元素。然后将当前元素入栈
"""


def nextGreaterElements(nums):
    N = len(nums)
    res = [-1] * N
    stack = []
    for i in range(N * 2):
        while stack and nums[stack[-1]] < nums[i % N]:
            res[stack.pop()] = nums[i % N]
        stack.append(i % N)
    return res
