"""
[销售价值减少的颜色球](https://leetcode-cn.com/problems/sell-diminishing-valued-colored-balls/)
"""


def maxProfit(inventory, orders: int) -> int:
    # 每次卖完之后，更新最大值列表
    res = 0
    mod = pow(10, 9) + 7
    init = 0
    while init != orders:
        tmp = max(inventory)
        res += tmp
        # 找到任意一个最大值的位置 - 1
        max_pos = inventory.index(tmp)
        inventory[max_pos] = tmp - 1
        init += 1
    return res % mod


if __name__ == '__main__':
    print(maxProfit([1000000000], 1000000000))
