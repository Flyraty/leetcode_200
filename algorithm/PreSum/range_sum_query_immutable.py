"""
[区域和检索 - 数组不可变](https://leetcode-cn.com/problems/range-sum-query-immutable)
前缀和系列，目的是找到时间复杂度较低的算法来算出 nums[i:j+1]，emmn，一开始写的就是 sum(nums[i:j+1])
"""


class NumArray:

    def __init__(self, nums):
        N = len(nums)
        self.preSum = [0] * (N + 1)
        for i in range(N):
            self.preSum[i + 1] = self.preSum[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.preSum[j + 1] - self.preSum[i]
