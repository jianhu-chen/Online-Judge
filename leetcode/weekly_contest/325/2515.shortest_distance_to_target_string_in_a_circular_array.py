#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://leetcode.cn/problems/shortest-distance-to-target-string-in-a-circular-array
from typing import List


class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        L, R = startIndex, startIndex
        step = 0
        while words[L] != target and words[R] != target and step <= n // 2:
            L = (L - 1 + n) % n
            R = (R + 1) % n
            step += 1
        if words[L] == target or words[R] == target:
            return step
        return -1
