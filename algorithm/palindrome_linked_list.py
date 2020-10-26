"""
[回文链表](https://leetcode-cn.com/problems/palindrome-linked-list/)

"""


def palindrome_linked_list(head):
    res = []
    while head:
        res.append(head)
        head = head.next

    return res == res.reverse()
