"""
[公平的糖果交换](https://leetcode-cn.com/problems/fair-candy-swap/)
sumA-x+y = sumB-y+x => sumA-sumB+2y = 2*x => x-y=(sumA-sumB) // 2。对于 x,y 存在上述关系则可以认为满足公平交换的条件
直接循环遍历判断上述等式是否成立时间复杂度太高，因此采用 hash 表的方式。
"""


def fair_candy_swap(A, B):
    sum_A = sum(A)
    sum_B = sum(B)
    delta = (sum_A - sum_B) // 2
    ans = None
    for y in B:
        x = y + delta
        if x in set(A):
            ans = [x, y]
            break
    return ans
