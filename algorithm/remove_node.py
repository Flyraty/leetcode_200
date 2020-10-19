"""
[删除链表的倒数第N个节点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/)
快慢指针，分别用两个指针指向头结点
first 快进N个节点
second
"""


class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def remove_node(head, n):
    length = len(head)
    dummy = ListNode(0, head)
    first = head
    second = dummy
    for i in range(length):
        first = first.next

    while first.next:
        first = first.next
        second.next = second.next
    second.next = second.next.next
    return dummy.next
