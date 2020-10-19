"""
[从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
[从中序与后序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
核心思想是找到根节点，根据根节点划分左右子树，递归解决
"""


class Tree:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def rebuild_tree(pre, middle):
    if pre:
        root = Tree(pre[0], None, None)
        root_pos = middle.index(pre[0])
        left_tree_size = len(middle[:root_pos])
        root.left = rebuild_tree(pre[1: left_tree_size + 1], middle[0:root_pos])
        root.right = rebuild_tree(pre[left_tree_size + 1:], middle[root_pos + 1:])

        return root


def rebuild_tree_1(middle, post):
    if middle:
        root = Tree(post[-1], None, None)
        root_pos = middle.index(post[-1])
        left_tree_size = len(middle[:root_pos])
        root.left = rebuild_tree(middle[0:root_pos], post[:left_tree_size])
        root.right = rebuild_tree(middle[root_pos+1:], post[left_tree_size+1:-2])
        return root


if __name__ == "__main__":
    print(rebuild_tree(pre=[3, 9, 20, 15, 7], middle=[9, 3, 15, 20, 7]))

