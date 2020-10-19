"""
[斐波那契数](https://leetcode-cn.com/problems/fibonacci-number/)
"""


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def fib1(n):
    dp = list()
    dp.append(0)
    dp.append(1)
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]


def fib2(n):
    if n < 2:
        return n
    pre1 = 1
    pre2 = 0
    cur = 0
    for i in range(2, n + 1):
        cur = pre1 + pre2
        pre2 = pre1
        pre1 = cur
    return cur


if __name__ == "__main__":
    print(fib(10))
    print(fib1(10))
    print(fib2(10))
