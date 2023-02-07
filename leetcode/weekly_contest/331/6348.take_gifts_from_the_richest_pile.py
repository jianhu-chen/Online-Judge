#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/take-gifts-from-the-richest-pile
import math
import heapq
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-x for x in gifts]
        heapq.heapify(heap)
        for _ in range(k):
            m = -heapq.heappop(heap)
            rest = math.floor(m ** 0.5)
            heapq.heappush(heap, -rest)
        return -sum(heap)
