"""
[独一无二的出现次数](https://leetcode-cn.com/problems/unique-number-of-occurrences/)
比较简单，count 统计，去重比较长度即可
"""


def uniqueOccurrences(arr) -> bool:
    counts = [arr.count(i) for i in set(arr)]
    return len(counts) == len(set(counts))
