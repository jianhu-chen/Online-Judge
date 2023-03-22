#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/best-team-with-no-conflicts
from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        a = sorted(zip(scores, ages), reverse=True)
        dp = [0] * n

        for i in range(n):
            for j in range(i):
                if a[i][1] <= a[j][1]:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += a[i][0]
        return max(dp)
