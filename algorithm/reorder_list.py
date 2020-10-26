"""
重排链表](https://leetcode-cn.com/problems/reorder-list/)
链表无法索引，将其存入到数据中，双指针遍历

"""


def reorder_list(head):
    nodes = []
    while head:
        nodes.append(head)
        head = head.next
    i, j = 0, len(nodes) - 1

    while i < j:
        nodes[i].next = nodes[j]
        i += 1
        if i == j:
            break
        nodes[j].next = nodes[i]
        j -= 1
    nodes[i].next = None