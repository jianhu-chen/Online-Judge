#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximum-average-pass-ratio
import heapq
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        classes = [(p / t - (p + 1) / (t + 1), p, t) for p, t in classes]
        heapq.heapify(classes)

        while extraStudents:
            _, p, t = heapq.heappop(classes)
            p += 1
            t += 1
            heapq.heappush(classes, (p / t - (p + 1) / (t + 1), p, t))
            extraStudents -= 1

        ans = 0
        for _, p, t in classes:
            ans += p / t
        return ans / len(classes)
