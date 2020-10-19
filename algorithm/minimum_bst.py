"""
[二叉搜索树的最小绝对差](https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/)
BST 前序遍历是一个递增序列，最小值的话肯定是两两相邻最小
"""


class Tree:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def minimum_bst(root):
    pre = 999
    diff = 999

    def search(root):
        nonlocal pre
        nonlocal diff
        if not root:
            return
        search(root.left)
        diff = min(diff, abs(pre - root.val))
        pre = root.val
        search(root.right)

    search(root)
    return diff


if __name__ == "__main__":
    root = Tree(8, None, Tree(3, Tree(1, None, None), None))
    print(minimum_bst(root))
