#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/design-graph-with-shortest-path-calculator
import heapq
from typing import List
from collections import defaultdict


class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.g = defaultdict(set)
        for u, v, c in edges:
            self.g[u].add((v, c))

    def addEdge(self, edge: List[int]) -> None:
        self.g[edge[0]].add((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        q = [(0, node1)]
        d = dict()
        while q:
            cost, u = heapq.heappop(q)
            if u in d:
                continue
            if u == node2:
                return cost
            d[u] = cost
            for v, c in self.g[u]:
                heapq.heappush(q, (cost + c, v))
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
