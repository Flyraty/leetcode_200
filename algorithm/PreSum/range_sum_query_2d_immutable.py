"""
[二维区域和检索 - 矩阵不可变](https://leetcode-cn.com/problems/range-sum-query-2d-immutable/)
由一维区域和检索得到，emmn，二维区域和检索可以由数学推理得到，没想出来
"""


class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        N = len(matrix[0]) if matrix else 0
        self.preSum = [[0] * (N + 1) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.preSum[i][j + 1] = self.preSum[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return sum([self.preSum[i][col2 + 1] - self.preSum[i][col1] for i in range(row1, row2 + 1)])


