#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    """https://codeforces.com/contest/1324/problem/E."""

    def sleepingSchedule(self, nums, h, L, R):
        return self.solution1(nums, h, L, R)

    def solution1(self, nums, h, L, R):
        n = len(nums)

        def dfs(i, t):
            c = 1 if t in range(L, R + 1) else 0
            if i == n:
                return c
            return max(
                dfs(i + 1, (t + nums[i]) % h),
                dfs(i + 1, (t + nums[i] - 1) % h)) + c

        return dfs(0, 0)

    def solution2(self, nums, h, L, R):
        n = len(nums)
        dp = [[0] * h for _ in range(n + 1)]

        return dp[0][0]


if __name__ == "__main__":
    _, h, L, R = map(int, input().split())
    nums = list(map(int, input().split()))
    print(Solution().sleepingSchedule(nums, h, L, R))
