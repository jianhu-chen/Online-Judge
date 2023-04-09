#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/shortest-cycle-in-a-graph
from math import inf
from typing import List
from collections import deque


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for s, t in edges:
            g[s].append(t)
            g[t].append(s)

        def bfs(start: int) -> int:
            ans = inf
            dis = [-1] * n  # dis[i] 表示从 start 到 i 的最短路长度
            dis[start] = 0
            q = deque([(start, -1)])
            while q:
                x, fa = q.popleft()
                for y in g[x]:
                    if dis[y] < 0:  # 第一次遇到
                        dis[y] = dis[x] + 1
                        q.append((y, x))
                    elif y != fa:  # 第二次遇到
                        ans = min(ans, dis[x] + dis[y] + 1)
            return ans

        ans = min(bfs(i) for i in range(n))
        return ans if ans < inf else -1
