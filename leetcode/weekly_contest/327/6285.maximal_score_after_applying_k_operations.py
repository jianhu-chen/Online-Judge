#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximal-score-after-applying-k-operations
import math
import heapq
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x: -x, nums))
        heapq.heapify(nums)
        score = 0
        while k > 0:
            top = heapq.heappop(nums)
            score += top
            heapq.heappush(nums, math.floor(top / 3))
            k -= 1
        return -score
