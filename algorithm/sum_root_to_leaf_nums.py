"""
[求根到叶子节点数字之和](https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/)
dfs，每个根节点到叶子节点组成的数字值可以看做是父节点的数字 * 10 + 当前节点的 value。

"""


def sumNumbers(root):
    def dfs(root, prevtotal):
        if not root: return 0
        total = prevtotal * 10 + root.val
        if not root.left and not root.right:
            return total
        return dfs(root.left, total) + dfs(root.right, total)

    return dfs(root, 0)