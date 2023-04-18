#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/flower-planting-with-no-adjacent
from typing import List


class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # 建图
        g = [[] for _ in range(n)]
        for u, v in paths:
            g[u - 1].append(v - 1)
            g[v - 1].append(u - 1)
        color = [0] * n
        for i, adj in enumerate(g):
            rest = {1, 2, 3, 4} - {color[j] for j in adj}
            color[i] = rest.pop()
        return color
