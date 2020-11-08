"""
二叉树的前序，中序，后序遍历的递归和非递归解法
"""


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def pre_order(root):
    res = []

    def preorder(root):
        res.append(root.val)
        preorder(root.left)
        preorder(root.right)

    preorder(root)
    return res


def pre_order_v1(root):
    res = []
    stack = []
    while stack or root:
        if root:
            res.append(root.val)
            stack.append(root)
            root = root.left
        else:
            root = stack.pop().right
    return res


def mid_order(root):
    res = []

    def midorder(root):
        midorder(root.left)
        res.append(root.val)
        midorder(root.right)

    midorder(root)
    return res


def mid_order_v1(root):
    res = []
    stack = []
    while root or stack:
        if root:
            root = root.left
            stack.append(root)
        else:
            res.append(root.value)
            root = stack.pop().right
    return res


def post_order(root):
    res = []

    def postorder(root):
        postorder(root.left)
        postorder(root.right)
        res.append(root.val)

    postorder(root)
    return res


### 看的大佬的颜色标记法

def post_order_v1(root):
    stack, res = [root], []
    while stack:
        i = stack.pop()
        if isinstance(i, TreeNode):
            stack.extend([i.val, i.right, i.left])
        elif isinstance(i, int):
            res.append(i)
    return res
