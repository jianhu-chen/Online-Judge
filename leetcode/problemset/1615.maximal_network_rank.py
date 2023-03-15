#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximal-network-rank
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g = [[0] * (n + 1) for _ in range(n)]
        for a, b in roads:
            g[a][b] = 1
            g[b][a] = 1
            g[a][-1] += 1
            g[b][-1] += 1

        return max(g[i][-1] + g[j][-1] - g[i][j] for i in range(n) for j in range(i + 1, n))
