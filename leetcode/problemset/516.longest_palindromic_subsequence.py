#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/longest-palindromic-subsequence

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestPalindromeSubseq2(s)

    def longestPalindromeSubseq1(self, s: str) -> int:
        def process(L, R):
            if L > R:
                return 0

            if L == R:
                return 1

            if s[L] == s[R]:
                return process(L + 1, R - 1) + 2
            else:
                return max(process(L + 1, R), process(L, R - 1))

        return process(0, len(s) - 1)

    def longestPalindromeSubseq2(self, s: str) -> int:
        # 动态规划
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]
