#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/minimize-the-total-price-of-the-trips
from typing import List
from collections import defaultdict


class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        # 建树
        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)

        # 统计trips需要经过每个节点的次数
        cnt = [0] * n
        for start, end in trips:
            def f(i, p):
                if i == end:
                    cnt[i] += 1
                    return True
                for j in g[i]:
                    if j != p and f(j, i):
                        cnt[i] += 1
                        return True
                return False
            f(start, -1)

        # 统计代价
        def dfs(i, p):
            no_halve = price[i] * cnt[i]
            halve = no_halve // 2
            for j in g[i]:
                if j == p:
                    continue
                nh, ha = dfs(j, i)
                no_halve += min(nh, ha)
                halve += nh
            return no_halve, halve

        return min(dfs(0, -1))
