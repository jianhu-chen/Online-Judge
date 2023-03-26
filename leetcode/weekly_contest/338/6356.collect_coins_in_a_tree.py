#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/collect-coins-in-a-tree
from typing import List
from collections import deque


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        """
        1. 拓扑排序: 去掉没有金币的子树
        2. 性质: 如果所有在叶子上的金币都收集到了, 那么所有金币都收集到了
        3. 再次拓扑排序, 去掉两轮叶子
        """
        # 先去掉没有金币的叶子结点
        n = len(coins)
        graph = [[] for _ in range(n)]
        degree = [0] * n
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
            degree[x] += 1
            degree[y] += 1

        q = deque()
        for i, (d, c) in enumerate(zip(degree, coins)):
            if d == 1 and c == 0:  # 没有金币的叶子
                q.append(i)

        left_edges = n - 1
        while q:
            x = q.popleft()
            left_edges -= 1
            for y in graph[x]:
                degree[y] -= 1
                if degree[y] == 1 and coins[y] == 0:  # 只有一个邻居, 是叶子
                    q.append(y)

        # 再跑两轮拓扑排序
        for i, (d, c) in enumerate(zip(degree, coins)):
            if d == 1 and c == 1:  # 有金币的叶子
                q.append(i)

        for x in q:
            left_edges -= 1
            for y in graph[x]:
                degree[y] -= 1
                if degree[y] == 1:
                    left_edges -= 1

        return max(left_edges * 2, 0)
