"""
[解码异或后的排列](https://leetcode-cn.com/problems/decode-xored-permutation/)
不得不说，一些基础数学知识已经很生疏了。参考 https://leetcode-cn.com/problems/decode-xored-permutation/solution/ji-shuang-yi-wen-dai-ni-shua-liang-dao-j-mujs/
"""


def decode(encoded):
    n = len(encoded)
    res = []
    first_all_xor = 0
    for i in range(1, n + 2):
        first_all_xor = first_all_xor ^ i
    all_xor = 0
    for i in range(1, n, 2):
        all_xor = all_xor ^ encoded[i]

    first = all_xor ^ first_all_xor
    res.append(first)

    for i in range(n):
        res.append(res[-1] ^ encoded[i])
    return res
