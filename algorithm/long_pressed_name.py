"""
[长按键入](https://leetcode-cn.com/problems/long-pressed-name/)
双指针
1. 确定指针移动条件，指向 name 的头指针i，指向 typed 的头指针j，指针位置值相等，
2. 确认边界，i 指针不用管，只会小于等于 j 指针，当 j 指针到尾部时，遍历结束，或者在遍历的过程中发现一个字符不匹配，就 break 跳出循环
"""


def pressed_name(name, typed):
    i, j = 0, 0
    while j < len(typed):
        if i < len(name) and name[i] == typed[j]:
            i += 1
            j += 1

        elif j > 0 and typed[j] == typed[j-1]:
            j += 1

        else:
            return False
    return True


