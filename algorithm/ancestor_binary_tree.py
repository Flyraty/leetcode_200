"""
[二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)
TODO
"""


def ancestor(root, p, q):
    if not root:
        return
    if root == p:
        return root
    if root == q:
        return root

    left = ancestor(root.left, p, q)
    right = ancestor(root.right, p, q)
    if left and right: return root
    if not left: return right
    if not right: return left
