"""
[视频拼接](https://leetcode-cn.com/problems/video-stitching/)
动态规划，自底之上，1 至少需要多少个拼接，2从1的基础上至少需要多少个拼接
"""

def stitch_video(clips, T):
    dp = [0] + [float("INF")] * T
    for i in range(1, T + 1):
        for aj, bj in clips:
            if aj < i <= bj:
                dp[i] = min(dp[i], dp[aj] + 1)
        return -1 if dp[T] == float("INF") else dp[T]
