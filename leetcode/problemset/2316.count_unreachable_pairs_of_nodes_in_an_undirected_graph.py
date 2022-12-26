#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph
from typing import Any, List


class DisjointSet:

    def __init__(self, nodes: List[Any]) -> None:
        self.parent = {n: n for n in nodes}
        self.rank = {n: 1 for n in nodes}

    def find(self, node: Any):
        path = []
        p = node
        while self.parent[p] != p:
            path.append(p)
            p = self.parent[p]
        while path:
            self.parent[path.pop()] = p
        return p

    def union(self, node1: Any, node2: Any):
        p1, p2 = self.find(node1), self.find(node2)
        if p1 == p2:
            return

        big = p1 if self.rank[p1] >= self.rank[p2] else p1
        small = p2 if big == p1 else p1
        self.parent[small] = big
        self.rank[big] += self.rank.pop(small)


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        d = DisjointSet(list(range(n)))
        for src, des in edges:
            d.union(src, des)
        result = 0
        total = 0
        for n in d.rank.values():
            result += total * n
            total += n
        return result
