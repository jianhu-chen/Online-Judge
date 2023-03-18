#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/find-score-of-an-array-after-marking-all-elements
from heapq import heapify, heappop
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        visited = set()
        heap = [(x, i) for i, x in enumerate(nums)]
        heapify(heap)
        ans = 0
        while len(visited) < len(nums):
            x, i = heappop(heap)
            if i in visited:
                continue
            visited |= {i - 1, i, i + 1}
            visited -= {-1, len(nums)}
            ans += x
        return ans
