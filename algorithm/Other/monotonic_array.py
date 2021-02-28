"""
[单调数组](https://leetcode-cn.com/problems/monotonic-array/)
两次遍历，一次判断是否递增，一次判断是否递减
一次遍历，打两个 flag 分别判断是否递增和递减，如果最终存在一个 flag 为 true，则是单调的
"""


def monotonic_array(A):
    def is_increase():
        for i in range(len(A) - 1):
            if (A[i + 1] - A[i]) < 0:
                return False
        return True

    def is_decrease():
        for i in range(len(A) - 1):
            if (A[i + 1] - A[i]) > 0:
                return False
        return True

    return is_decrease() or is_increase()


def monotonic_array_v2(A):
    inc, dec = True, True
    for i in range(len(A) - 1):
        if (A[i + 1] - A[i]) < 0:
            inc = False

    for i in range(len(A) - 1):
        if (A[i + 1] - A[i]) > 0:
            dec = False

    return inc or dec


if __name__ == '__main__':
    A = [1, 3, 2]
    print(monotonic_array(A))
    print(monotonic_array_v2(A))