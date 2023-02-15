#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/maximum-number-of-pairs-in-array
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cnt, visited = 0, set()
        for x in nums:
            if x not in visited:
                visited.add(x)
            else:
                cnt += 1
                visited.remove(x)
        return cnt, len(visited)
