#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/count-subtrees-with-max-distance-between-cities
from typing import List


class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # 建树
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)  # 编号改为从 0 开始

        # 计算树上任意两点的距离
        dis = [[0] * n for _ in range(n)]

        def dfs(x: int, fa: int) -> None:
            for y in g[x]:
                if y != fa:
                    dis[i][y] = dis[i][x] + 1  # 自顶向下
                    dfs(y, x)
        for i in range(n):
            dfs(i, -1)  # 计算 i 到其余点的距离

        def dfs2(x: int, fa: int) -> int:
            # 能递归到这，说明 x 可以选
            cnt = 1  # 选 x
            for y in g[x]:
                if y != fa and \
                   (di[y] < d or di[y] == d and y > j) and \
                   (dj[y] < d or dj[y] == d and y > i):  # 满足这些条件就可以选
                    cnt *= dfs2(y, x)  # 每棵子树互相独立，采用乘法原理
            if di[x] + dj[x] > d:  # x 是可选点
                cnt += 1  # 不选 x
            return cnt
        ans = [0] * (n - 1)
        for i, di in enumerate(dis):
            for j in range(i + 1, n):
                dj = dis[j]
                d = di[j]
                ans[d - 1] += dfs2(i, -1)
        return ans
