"""
[比较含退格的字符串](https://leetcode-cn.com/problems/backspace-string-compare/)
还原两个字符串，判断是否相等
"""


def backspace_compare(str1, str2):
    """
    :param str1: "a##b"
    :param str2: "b"
    :return:
    """

    def pre_compare(x):
        s = []
        for i in x:
            if i == "#":
                if s:
                    s.pop()
                    continue
                else:
                    continue
            s.append(i)
        return "".join(s)

    str1_ = pre_compare(str1)
    str2_ = pre_compare(str2)
    return str1_ == str2_


if __name__ == '__main__':
    print(backspace_compare("a##b", "a##b"))
    print(backspace_compare("ab#c", "abc"))
