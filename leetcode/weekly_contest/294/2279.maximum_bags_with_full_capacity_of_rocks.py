#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximum-bags-with-full-capacity-of-rocks
from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff = [capacity[i] - rocks[i] for i in range(len(capacity))]
        diff.sort()
        cnt = 0
        for d in diff:
            if d == 0:
                cnt += 1
            elif d <= additionalRocks:
                cnt += 1
                additionalRocks -= d
            else:
                break
        return cnt
