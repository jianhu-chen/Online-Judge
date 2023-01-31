#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/put-marbles-in-bags
import heapq
from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        return self.solution2(weights, k)

    def solution1(self, weights: List[int], k: int) -> int:
        """堆."""
        n = len(weights)
        heap1, heap2 = [], []
        for i in range(n - 1):
            w = weights[i] + weights[i + 1]
            heapq.heappush(heap1, w)
            heapq.heappush(heap2, -w)
        diff = 0
        for _ in range(k - 1):
            diff += -heapq.heappop(heap2)
            diff -= heapq.heappop(heap1)
        return diff

    def solution2(self, weights: List[int], k: int) -> int:
        """排序."""
        s = []
        n = len(weights)
        for i in range(n - 1):
            w = weights[i] + weights[i + 1]
            s.append(w)
        s.sort()
        return sum(s[-(k - 1):]) - sum(s[:(k - 1)]) if k > 1 else 0
