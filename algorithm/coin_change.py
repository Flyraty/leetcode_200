"""
[零钱兑换](https://leetcode-cn.com/problems/coin-change/)
"""


# 这种方法在 leetcode 上超时了
def coin_change(coins, amount):
    def dp(n):
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float('INF')
        for coin in coins:
            sub_problem = dp(n - coin)
            if sub_problem == -1:
                continue
            res = min(res, 1 + sub_problem)
        return res if res != float('INF') else -1

    return dp(amount)


# 缓存重复计算结果
def coin_change1(coins, amount):
    memo = dict()

    def dp(n):
        if n in memo.keys(): return memo[n]
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = float('INF')
        for coin in coins:
            sub_problem = dp(n - coin)
            if sub_problem == -1:
                continue
            res = min(res, 1 + sub_problem)
        memo[n] = res if res != float('INF') else -1
        return memo[n]

    return dp(amount)


if __name__ == "__main__":
    print(coin_change([1, 2, 5], 11))
    print(coin_change1([1, 2, 5], 11))
