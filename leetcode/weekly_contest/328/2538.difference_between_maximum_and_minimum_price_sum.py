#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/difference-between-maximum-and-minimum-price-sum
from typing import List
from collections import defaultdict


class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        return self.solution2(n, edges, price)

    def solution1(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        """DFS."""
        if n < 2:
            return 0

        degree = {}
        nexts = defaultdict(set)  # 邻节点
        for s, t in edges:
            degree[s] = degree.get(s, 0) + 1
            degree[t] = degree.get(t, 0) + 1
            nexts[s].add(t)
            nexts[t].add(s)

        def dfs(s, pa):
            """s: 起始节点编号."""
            ans = 0
            for n in nexts[s]:
                if n == pa:
                    continue
                ans = max(ans, dfs(n, s))
            return ans + price[s]

        ans = 0
        for i in range(n):
            # 从 i 出发的开销
            if degree[i] != 1:
                continue
            ans = max(ans, dfs(i, None) - price[i])

        return ans

    def solution2(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        """树形dp."""
        if n < 2:
            return 0

        nexts = defaultdict(set)  # 邻节点
        for s, t in edges:
            nexts[s].add(t)
            nexts[t].add(s)

        def dfs(i, pa):
            """返回带叶子结点的最大路径和，不带叶子结点的最大路径和, 以及答案."""
            m1, m2, ans = price[i], 0, 0
            for n in nexts[i]:
                if n == pa:
                    continue
                cm1, cm2, cans = dfs(n, i)
                # m1 + cm2: 前面最大带叶子结点的路径和 + 当前不带叶子结点的路径和
                # m2 + cm1: 前面最大不带叶子结点的路径和 + 当前带叶子结点的路径和
                ans = max(ans, cans, m1 + cm2, m2 + cm1)
                m1 = max(m1, cm1 + price[i])
                m2 = max(m2, cm2 + price[i])
            return m1, m2, ans

        # 以 0 作为 root
        return dfs(0, None)[2]
