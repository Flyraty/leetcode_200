"""
[二叉树的序列化与反序列化](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/)
需要注意的是，序列化过程中，叶子节点会产生多余的 None
"""
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return []
        queue = collections.deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        print(res)
        while not res[-1]:
            res.pop()
        print(res)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        node_ = [TreeNode(val, None, None) for val in data]
        flag = 2
        for i in range(0, len(node_)):
            if flag + 1 > len(node_):
                break
            node_[i].left = node_[flag - 1]
            node_[i].right = node_[flag]
            flag += 2
        return node_[0]

# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
