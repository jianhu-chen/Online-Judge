#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/count-number-of-possible-root-nodes
from typing import List


class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        # 构图
        g = [[] for _ in range(len(edges) + 1)]
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)

        s = set(map(tuple, guesses))

        cnt0 = 0

        def dfs(i, p):
            """计算以 i 为根节点时, bob 猜对了几次."""
            nonlocal cnt0
            for nxt in g[i]:
                if nxt == p:
                    continue
                cnt0 += (i, nxt) in s
                dfs(nxt, i)
        dfs(0, None)

        ans = 0

        def reroot(i, p, cnt):
            """换根测试, 统计满足条件的根结点数目."""
            nonlocal ans
            ans += cnt >= k  # 满足条件, 计数+1
            for nxt in g[i]:  # 换根测试
                if nxt == p:
                    continue
                # 交换 i 与 nxt
                reroot(nxt, i, cnt - ((i, nxt) in s) + ((nxt, i) in s))

        reroot(0, None, cnt0)
        return ans
