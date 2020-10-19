"""
[两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)
temp -> node1 -> node2 => temp -> node2 -> node1

temp.next = node2
node1.next = node2.next
node2.next = node1
"""


class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def node_change(head):
    dummpy_node = ListNode(0, None)
    dummpy_node.next = head
    temp = dummpy_node
    while temp.next and temp.next.next:
        node1 = temp.next
        node2 = temp.next.next
        temp.next = node2
        node1.next = node2.next
        node2.next = node1
        temp = node1
    return dummpy_node.next


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, None)))
    print(node_change(head).next.val)