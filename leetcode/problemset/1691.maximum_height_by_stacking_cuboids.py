#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximum-height-by-stacking-cuboids
from typing import List
from itertools import permutations


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        """暴力+动态规划."""
        for x in cuboids:
            x.sort()
        cuboids.sort()
        f = [[0] * 6 for _ in range(len(cuboids))]
        for i, c1 in enumerate(cuboids):
            for j, (w1, l1, h1) in enumerate(permutations(c1)):
                for k, c2 in enumerate(cuboids[:i]):
                    for l, (w2, l2, h2) in enumerate(permutations(c2)):
                        if w2 <= w1 and l2 <= l1 and h2 <= h1:
                            f[i][j] = max(f[i][j], f[k][l])
                f[i][j] += h1
        return max(max(x) for x in f)
