"""
[绝对差不超过限制的最长连续子数组](https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit)

"""
from sortedcontainers import SortedList


def longestSubarray(nums, limit):
    s = SortedList()
    n = len(nums)
    left = right = ret = 0

    # 滑动窗口，找寻所有符合条件的子数组，求最长
    while right < n:
        s.add(nums[right])
        while s[-1] - s[0] > limit:
            s.remove(nums[left])
            left += 1
        ret = max(ret, right - left + 1)
        right += 1

    return ret


if __name__ == '__main__':
    print(longestSubarray([1, 2, 3, 4], 1))
