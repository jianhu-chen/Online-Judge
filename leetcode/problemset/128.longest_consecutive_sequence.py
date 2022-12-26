#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/longest-consecutive-sequence
from typing import Any, List


class DisjointSet:

    def __init__(self, nodes: List[Any]) -> None:
        self.parent = {n: n for n in nodes}
        self.rank = {n: 1 for n in nodes}

    def find(self, node: Any):
        path = []
        p = node
        while p != self.parent[p]:
            path.append(p)
            p = self.parent[p]

        while path:
            self.parent[path.pop()] = p
        return p

    def is_same_set(self, node1: Any, node2: Any):
        return self.find(node1) == self.find(node2)

    def union(self, node1: Any, node2: Any):
        p1 = self.find(node1)
        p2 = self.find(node2)

        if p1 == p2:
            return

        big = p1 if self.rank[p1] > self.rank[p2] else p2
        small = p2 if big == p1 else p1
        self.parent[small] = big
        self.rank[big] += self.rank.pop(small)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return self.longestConsecutive2(nums)

    def longestConsecutive1(self, nums: List[int]) -> int:
        """方法1."""
        s = set(nums)

        result = 0
        for n in s:
            if n - 1 in s:
                continue

            x = n
            maybe_result = 0
            while x in s:
                maybe_result += 1
                x += 1

            if maybe_result > result:
                result = maybe_result

        return result

    def longestConsecutive2(self, nums: List[int]) -> int:
        """方法2: 并查集."""
        if not nums:
            return 0

        s = set(nums)
        d = DisjointSet(s)

        for n in s:
            if n - 1 in s:
                d.union(n, n - 1)
            if n + 1 in s:
                d.union(n, n + 1)
        return max(d.rank.values())
