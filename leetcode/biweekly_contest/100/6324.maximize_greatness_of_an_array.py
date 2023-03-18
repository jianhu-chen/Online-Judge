#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximize-greatness-of-an-array
from heapq import heapify, heappop
from typing import List


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        h1, h2 = nums, nums[::]  # deepcopy
        heapify(h1)
        heapify(h2)
        cnt = 0
        while h1 and h2:
            top = heappop(h1)
            while h2 and h2[0] <= top:
                heappop(h2)
            if h2:
                heappop(h2)
                cnt += 1
        return cnt
