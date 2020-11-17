"""
[岛屿的周长](https://leetcode-cn.com/problems/island-perimeter/)
前提条件是岛中不存在湖，从(0, 0) 开始遍历，假设开始处就是岛屿，那么周长加 4，如果其下边或者右边也是岛屿，会合并掉两条边，所以岛屿周长需要减 2。以此往复，遍历所有网格。
"""


def islandPerimeter(grid):
    if not grid:
        return 0
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                res += 4
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    res -= 2
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    res -= 2
    return res
