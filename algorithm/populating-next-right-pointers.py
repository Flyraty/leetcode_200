"""
[填充每个节点的下一个右侧节点指针](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/)
[填充每个节点的下一个右侧节点指针 II](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/)

BFS 广度优先遍历，依靠 queue
"""
import collections


def fill_node_right(root):
    if not root:
        return root
    queue = collections.deque([root])

    while queue:
        length = len(queue)
        for i in range(length):
            node = queue.popleft()
            if i < length - 1:
                node.next = queue[0]
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return root


if __name__ == "__main__":
    pass
